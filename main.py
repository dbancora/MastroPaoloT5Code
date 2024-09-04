# Install necessary libraries
#pip install transformers==4.44.2
#pip install nlp==0.4.0
#pip install pyarrow==0.16.0
#pip install sentencepiece==0.1.96
#pip install dill==0.3.3

#pip install numpy==1.26.4

import torch
import nlp
from tqdm import tqdm
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration
import pandas as pd
import os


# Define file paths
spm_path = 'T5-Extension/Tokenizer/dl4se.model'
config_file = 'T5-Extension/Trained-Models/with-pretraining-new/MT-Task-Balanced/Pytorch-Model/config.json'
#Modifica il path del file tsv che contiene i metodi da predire
test_file = 'T5-Extension/Datasets/tsv/fine-tuning/AGraw/results_2023_methods_None_JUnit 5.tsv'
finetuned_model_path = 'T5-Extension/Trained-Models/with-pretraining-new/MT-Task-Balanced/Pytorch-Model/pytorch_model.bin'
#Modifica il nome del file di output
prediction_output_path = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/prediction_2023_JUnit5_@{}.txt'
#Modifica il nome del file di output
perfect_prediction_output_path = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/perfect2023_JUnit5_@{}.txt'

# Load tokenizer and config
config = T5Config.from_json_file(config_file)
tokenizer = T5Tokenizer.from_pretrained(spm_path)



def add_eos_to_examples(example):
    example['input_text'] = 'generate raw assert: %s ' % example['method']#.lower()
    example['target_text'] = '%s ' % example['assertion']#.lower()
    return example

def convert_to_features(example_batch):
    input_encodings = tokenizer.batch_encode_plus(example_batch['input_text'], pad_to_max_length=True, max_length=512)
    target_encodings = tokenizer.batch_encode_plus(example_batch['target_text'], pad_to_max_length=True, max_length=512)

    encodings = {
        'input_ids': input_encodings['input_ids'],
        'attention_mask': input_encodings['attention_mask'],
        'target_ids': target_encodings['input_ids'],
        'target_attention_mask': target_encodings['attention_mask']
    }

    return encodings

# Specifica la nuova directory di cache
new_cache_dir = 'T5-Extension/Cache'

# Crea la directory se non esiste
os.makedirs(new_cache_dir, exist_ok=True)
# Load dataset script and dataset
# Adjust the path of the dataset script according to your local filesystem


import shutil

# Definisci il percorso del file di origine e di destinazione
source_path = 'T5-Extension/Datasets/tsv/fine-tuning/AGraw/results_2020_methods_None_JUnit 5.tsv'
destination_path = 'test.tsv'

# Copia il file dal percorso di origine al percorso di destinazione
shutil.copy(source_path, destination_path)

valid_dataset = nlp.load_dataset('T5-Extension/Miscellaneous/assertion_dataset_script.py', split=nlp.Split.TEST, cache_dir=new_cache_dir)



# Map functions to dataset
valid_dataset = valid_dataset.map(add_eos_to_examples, load_from_cache_file=False, keep_in_memory=True)


valid_dataset = valid_dataset.map(convert_to_features, batched=True, load_from_cache_file=False, keep_in_memory=True)

columns = ['input_ids', 'target_ids', 'attention_mask', 'target_attention_mask']
valid_dataset.set_format(type='torch', columns=columns)

BATCH_SIZE = 12
dataloader = torch.utils.data.DataLoader(valid_dataset, batch_size=BATCH_SIZE)

# Load ground truth from the test dataset
df = pd.read_csv(test_file, header=None, sep='\t')

references = [item for item in df[1]]
inputs = [item for item in df[0]]

inputs[0], references[0]

# Set CUDA device
print(f"La GPU è disponibile e pronta: {torch.cuda.is_available()}")
CUDA = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = T5ForConditionalGeneration.from_pretrained(
        finetuned_model_path,
        config=config
        ).to(CUDA)

model.eval()

predictions = []
BEAM_SIZE = 10

torch.cuda.empty_cache()

for batch in tqdm(dataloader):
    outs = model.generate(
        input_ids=batch['input_ids'].to(CUDA),
        attention_mask=batch['attention_mask'].to(CUDA),
        num_beams=BEAM_SIZE,
        max_length=512,
        num_return_sequences=BEAM_SIZE,
        early_stopping=True
    )
    outs = [tokenizer.decode(ids, skip_special_tokens=True) for ids in outs]
    predictions.extend(outs)

pred_refined = []
for pred in predictions:
    if len(pred) >= 2:
        if pred[0] == '"':
            pred = pred[1:]
        if pred[-1] == '"':
            pred = pred[:-1]
    pred_refined.append(pred)

import re

def remove_substring_case_insensitive(text, substring):
    """Rimuove il substring dalla text in modo case-insensitive."""
    pattern = re.compile(re.escape(substring), re.IGNORECASE)
    return pattern.sub('', text)

# Parte della stringa che si desidera rimuovere
part_to_remove = "org.junit.Assert."

counter_pred = 0
mispred_list = []
sanity_check_list = []
idx = 0
len_prediction = len(pred_refined)

# Apri il file di output delle predizioni con encoding UTF-8
with open(prediction_output_path.format(BEAM_SIZE), 'a+', encoding='utf-8') as fpred:
    for i in range(0, len_prediction, BEAM_SIZE):
        items_to_analyze = pred_refined[i:i+BEAM_SIZE]
        target_item = ''.join(references[idx].split(' '))

        flag_perfect = False

        fpred.write('************************************\n')
        fpred.write('[+] input: {}\n'.format(inputs[idx]))

        for pred in items_to_analyze:
            # Rimuove "org.junit.Assert." dalla predizione in modo case-insensitive
            pred_ref = ''.join(pred.split(' '))
            pred_ref = remove_substring_case_insensitive(pred_ref, part_to_remove)

            #print(pred_ref)  # Stampa pred_ref per verificare la rimozione

            fpred.write('[*] target: {}\n'.format(references[idx]))
            fpred.write('[-] pred:  {}\n\n'.format(pred))

            # Confronto tra predizione (senza "org.junit.Assert.") e target
            if pred_ref == target_item and not flag_perfect:
                counter_pred += 1
                sanity_check_list.append(pred)

                with open(perfect_prediction_output_path.format(BEAM_SIZE), 'a+', encoding='utf-8') as fwrite:
                    fwrite.write('[+] input: {}\n'.format(inputs[idx]))
                    fwrite.write('[*] target: {}\n'.format(references[idx]))
                    fwrite.write('[-] pred:  {}\n\n'.format(pred))

                flag_perfect = True
            else:
                mispred_list.append(pred)

        fpred.write('************************************\n')
        idx += 1

# Stampa i risultati
print('% of perfect predictions: ', (counter_pred / len(references)) * 100)
print(counter_pred)

