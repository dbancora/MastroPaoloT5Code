#
# import re
#
# def elimina_ripetizioni(file_path):
#     """Funzione per filtrare le coppie input-target nel file filtrato e contare le ripetizioni"""
#     coppie_uniche = set()  # Per salvare le coppie uniche
#     coppie_duplicate_set = set()  # Per salvare le coppie duplicate
#     totale_coppie = 0  # Conta tutte le coppie trovate
#     coppie_duplicate = 0  # Conta le coppie duplicate
#
#     # **Pattern aggiornati per catturare contenuti multi-linea**
#     pattern_input = re.compile(r'\[\+\] input:\s*(.*?)\s*(?=\[\*\] target:|\[-\] pred:|$)', re.DOTALL)
#     pattern_target = re.compile(r'\[\*\] target:\s*(.*?)\s*(?=\[-\] pred:|\[\+\] input:|$)', re.DOTALL)
#     pattern_pred = re.compile(r'\[-\] pred:\s*(.*?)\s*(?=\[\+\] input:|\[\*\] target:|$)', re.DOTALL)
#
#     with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
#         contenuto = file.read()
#
#         # Cerca tutti i blocchi di input, target e pred
#         input_matches = pattern_input.findall(contenuto)
#         target_matches = pattern_target.findall(contenuto)
#         pred_matches = pattern_pred.findall(contenuto)
#
#         # Assicurati che il numero di input, target e pred corrisponda
#         if len(input_matches) != len(target_matches) or len(input_matches) != len(pred_matches):
#             print("Il numero di input, target e pred non corrisponde!")
#             return coppie_uniche, coppie_duplicate_set, totale_coppie, coppie_duplicate
#
#         # Combina input, target e pred in coppie uniche
#         for input_value, target_value, pred_value in zip(input_matches, target_matches, pred_matches):
#             totale_coppie += 1  # Conta ogni coppia trovata
#             coppia = (input_value.strip(), target_value.strip(), pred_value.strip())
#             if coppia in coppie_uniche:
#                 coppie_duplicate += 1  # Incrementa se la coppia è già nel set (duplicata)
#                 coppie_duplicate_set.add(coppia)  # Aggiungi alla lista delle duplicazioni
#             else:
#                 coppie_uniche.add(coppia)  # Aggiunge la coppia unica
#
#     return coppie_uniche, coppie_duplicate_set, totale_coppie, coppie_duplicate
#
#
# def salva_file_filtrato(coppie_uniche, output_path):
#     """Funzione per salvare le coppie filtrate in un file"""
#     with open(output_path, 'w', encoding='utf-8') as file:
#         for input_value, target_value, pred_value in coppie_uniche:
#             file.write(f"[+] input: {input_value}\n")
#             file.write(f"[*] target: {target_value}\n")
#             file.write(f"[-] pred: {pred_value}\n")
#             file.write("************************************\n************************************\n")
#     print(f"File filtrato salvato in: {output_path}")
#
#
# def conta_elementi_file_confronto(file_path):
#     """Funzione per contare quanti blocchi di predizione ci sono nel file di confronto"""
#     blocchi_confronto = []
#
#     with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
#         contenuto = file.read()
#         # Dividi i blocchi usando il nuovo separatore di asterischi consecutivi
#         blocchi_confronto = contenuto.split("************************************\n************************************")
#         # Rimuovi blocchi vuoti o spazi bianchi
#         blocchi_confronto = [blocco.strip() for blocco in blocchi_confronto if blocco.strip()]
#
#     return blocchi_confronto
#
#
# def calcola_proporzione(file_filtrato, file_confronto, file_output_filtrato):
#     # Ottieni le coppie uniche, il numero di coppie e le ripetizioni nel file filtrato
#     coppie_filtrate, coppie_duplicate_set, totale_filtrato, duplicate_filtrato = elimina_ripetizioni(file_filtrato)
#
#     # Salva il file filtrato
#     salva_file_filtrato(coppie_filtrate, file_output_filtrato)
#
#     # Ottieni i blocchi dal file di confronto
#     blocchi_confronto = conta_elementi_file_confronto(file_confronto)
#     totale_confronto = len(blocchi_confronto)  # Numero di blocchi nel file di confronto
#
#     # Conta quanti blocchi del file di confronto hanno una corrispondenza nel file filtrato
#     num_coppie_comuni = 0
#
#     # **Aggiorna i pattern anche qui per catturare contenuti multi-linea**
#     pattern_input = re.compile(r'\[\+\] input:\s*(.*?)\s*(?=\[\*\] target:|\[-\] pred:|$)', re.DOTALL)
#     pattern_target = re.compile(r'\[\*\] target:\s*(.*?)\s*(?=\[-\] pred:|\[\+\] input:|$)', re.DOTALL)
#
#     for blocco in blocchi_confronto:
#         input_match = pattern_input.search(blocco)
#         target_match = pattern_target.search(blocco)
#
#         if input_match and target_match:
#             input_value = input_match.group(1).strip()
#             target_value = target_match.group(1).strip()
#             # Pred non è usato qui per il confronto
#             coppia = (input_value, target_value)
#
#             # Cerca solo input-target nel set delle coppie filtrate
#             if any((input_value == coppia_f[0] and target_value == coppia_f[1]) for coppia_f in coppie_filtrate):
#                 num_coppie_comuni += 1
#
#     # Calcola la proporzione rispetto al file di confronto
#     if totale_confronto == 0:
#         proporzione = 0.0
#     else:
#         proporzione = (num_coppie_comuni / totale_confronto) * 100
#
#     # Mostra il risultato
#     print(f"Totale coppie trovate nel file filtrato: {totale_filtrato}")
#     print(f"Numero di coppie duplicate eliminate: {duplicate_filtrato}")
#     print(f"Numero di coppie uniche nel file filtrato: {len(coppie_filtrate)}")
#     print(f"NUMERO DI PLACEHOLDER CORRETTI: {num_coppie_comuni}")
#     print(f"Totale blocchi nel file di confronto: {totale_confronto}")
#     print(f"Proporzione di blocchi del file di confronto presenti nel file filtrato: {proporzione:.3f}%")
#
#     # Stampa le coppie duplicate
#     if coppie_duplicate_set:
#         print("\nCoppie duplicate trovate:")
#         #for input_value, target_value, pred_value in coppie_duplicate_set:
#             #print(f"[+] input: {input_value}")
#             #print(f"[*] target: {target_value}")
#             #print(f"[-] pred: {pred_value}")
#             #print("************************************\n************************************")
#
#
# def main():
#     # Questo script controlla se le asserzioni presenti nel file di confronto sono contenute anche nel file perfect, così da creare un file perfect seza ripetizioni
#     # Specifica il percorso dei file direttamente
#     file_filtrato = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/perfect2022_JUnit4_@1.txt'
#     # In questi due file puoi modificare tra "OneAssert" e "MultiAssert" in modo da verificare i placeholder corretti e la percentuale
#     file_confronto = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2022_JUnit4_OneAssert_@1.txt'
#     file_output_filtrato = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_perfect2022_JUnit4_OneAssert_@1.txt'  # File dove verrà salvato il filtrato
#
#     # Esegui la funzione di calcolo della proporzione
#     calcola_proporzione(file_filtrato, file_confronto, file_output_filtrato)
#
#
# if __name__ == "__main__":
#     main()
#

# QUESTO SCRIPT E' UTILE PER CREARE IL PERFECT MULTIASSERT CHE NON ABBIAMO OTTENUTO DAL MODELLO

import re

def extract_triplets(file_path):
    """
    Estrae tutte le triplette (input, target, pred) da un file.
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()

    # Espressioni regolari per identificare input, target e pred
    pattern_input = re.compile(r'\[\+\] input:\s*(.*?)\s*(?=\[\*\] target:|\[\+\] input:|$)', re.DOTALL)
    pattern_target = re.compile(r'\[\*\] target:\s*(.*?)\s*(?=\[-\] pred:|\[\*\] target:|$)', re.DOTALL)
    pattern_pred = re.compile(r'\[-\] pred:\s*(.*?)\s*(?=\[\+\] input:|\[-\] pred:|$)', re.DOTALL)

    # Trova tutte le occorrenze
    inputs = pattern_input.findall(content)
    targets = pattern_target.findall(content)
    preds = pattern_pred.findall(content)

    # Verifica che il numero di input, target e pred corrisponda
    if len(inputs) != len(targets) or len(inputs) != len(preds):
        print("Errore! Numero di input, target e pred non corrispondono!")
        print(f"Input trovati: {len(inputs)}, Target trovati: {len(targets)}, Pred trovati: {len(preds)}")
        return []

    # Combina le triplette
    triplets = list(zip(inputs, targets, preds))

    # Debug: Stampa le prime 5 triplette estratte
    print(f"Triplette estratte dal file {file_path}:")
    for triplet in triplets[:5]:
        print(triplet)
    print(f"Totale triplette estratte: {len(triplets)}\n")

    return triplets

def extract_first_input_target(file_path):
    """
    Estrae solo la prima coppia (input, target) per ogni input da file_predictions.
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()

    # Dividi il contenuto in blocchi separati da '************************************'
    blocks = re.split(r'\*{36,}', content)  # Assume almeno 36 '*' come separatore

    first_pairs = []
    for block_num, block in enumerate(blocks, start=1):
        block = block.strip()
        if not block:
            continue

        # Estrai l'input
        input_match = re.search(r'\[\+\] input:\s*(.*?)\s*(?=\[\*\] target:|\[\+\] input:|$)', block, re.DOTALL)
        if not input_match:
            print(f"Input non trovato nel blocco {block_num} in {file_path}.")
            continue
        input_value = input_match.group(1).strip()

        # Estrai tutti i target nel blocco
        targets = re.findall(r'\[\*\] target:\s*(.*?)\s*(?=\[-\] pred:|\[\*\] target:|$)', block, re.DOTALL)
        if not targets:
            print(f"Target non trovato nel blocco {block_num} con input: {input_value}")
            continue
        first_target = targets[0].strip()

        # Aggiungi la coppia (input, target)
        first_pairs.append((input_value, first_target))

    # Debug: Stampa le prime 5 coppie estratte
    print(f"Coppie estratte da {file_path} (solo la prima per input):")
    for pair in first_pairs[:5]:
        print(pair)
    print(f"Totale coppie estratte: {len(first_pairs)}\n")

    return first_pairs

def save_common_triplets(file_path, common_triplets):
    """
    Salva le triplette comuni in un file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for input_value, target_value, pred_value in common_triplets:
            file.write(f"[+] input: {input_value}\n")
            file.write(f"[*] target: {target_value}\n")
            file.write(f"[-] pred: {pred_value}\n")
            file.write("************************************\n************************************\n")
    print(f"File salvato in: {file_path}")

def main():
    # Percorsi dei file di input
    file_perfect = "T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/perfect2024_JUnit5_@10.txt"
    file_predictions = "T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2024_JUnit5_MultiAssert_@10.txt"

    # Percorso del file di output
    file_output = "T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_perfect2024_JUnit5_MultiAssert_@10.txt"

    # Estrai le triplette da file_perfect
    print("Estrazione delle triplette da file_perfect...")
    triplets_perfect = extract_triplets(file_perfect)

    # Crea un dizionario che mappa (input, target) a pred da file_perfect
    perfect_dict = {}
    for input_val, target_val, pred_val in triplets_perfect:
        key = (input_val, target_val)
        perfect_dict[key] = pred_val

    print(f"Numero di coppie (input, target) in file_perfect: {len(perfect_dict)}\n")

    # Estrai le coppie (input, target) da file_predictions
    print("Estrazione delle coppie (input, target) da file_predictions...")
    prediction_pairs = extract_first_input_target(file_predictions)

    # Trova le coppie comuni
    common_pairs = []
    for pair in prediction_pairs:
        if pair in perfect_dict:
            pred_val = perfect_dict[pair]
            common_pairs.append((pair[0], pair[1], pred_val))

    print(f"Numero di coppie comuni trovate: {len(common_pairs)}\n")

    # Debug: Stampa le prime 5 triplette comuni trovate
    if common_pairs:
        print("Triplette comuni trovate:")
        for triplet in common_pairs[:5]:
            print(triplet)
        print()
    else:
        print("Nessuna triplet comune trovata.\n")

    # Salva le triplette comuni nel file di output
    if common_pairs:
        save_common_triplets(file_output, common_pairs)
    else:
        print("Nessuna triplet comune da salvare.")

    # Opzionale: Stampa le triplette non corrispondenti per debug
    unmatched_pairs = [pair for pair in prediction_pairs if pair not in perfect_dict]
    print(f"Numero di coppie non corrispondenti: {len(unmatched_pairs)}")
    if unmatched_pairs:
        print("Esempi di coppie non corrispondenti:")
        for pair in unmatched_pairs[:5]:
            print(pair)
    print()

if __name__ == "__main__":
    main()
