import re

def parse_entries(filename):
    entries = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dividi il contenuto in base alle linee di asterischi
    raw_entries = re.split(r'\n\*{36}\n', content.strip())

    for raw_entry in raw_entries:
        raw_entry = raw_entry.strip()
        if not raw_entry:
            continue
        # Estrai le linee [+] input, [*] target, [-] pred
        input_line = target_line = pred_line = ''
        lines = raw_entry.split('\n')
        for line in lines:
            if line.startswith('[+] input:'):
                input_line = line.strip()
            elif line.startswith('[*] target:'):
                target_line = line.strip()
            elif line.startswith('[-] pred:'):
                pred_line = line.strip()
        # Crea un identificatore unico per l'entry
        entry_key = '\n'.join([input_line, target_line, pred_line])
        entries.append((entry_key, raw_entry))
    return entries
# CAMBIA SOLO IL BEAM SIZE, versione di JUnit e anno. Non toccare altro
def main():
    file_a = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2024_JUnit5_@10.txt'
    file_b = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2024_JUnit5_OneAssert_@10.txt'
    output_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2024_JUnit5_MultiAssert_@10.txt'

    # Parsea le voci dai file
    entries_a = parse_entries(file_a)
    entries_b = parse_entries(file_b)

    # Crea un set di chiavi per le voci nel file B
    entries_b_keys = set(entry[0] for entry in entries_b)

    # Trova le voci nel file A che non sono presenti in B
    entries_diff = [entry for entry in entries_a if entry[0] not in entries_b_keys]

    # Conta il numero di voci trovate
    num_entries = len(entries_diff)
    print(f"Numero di voci trovate: {num_entries}")

    # Scrivi le voci rimanenti nel file di output
    with open(output_file, 'w', encoding='utf-8') as f:
        for _, raw_entry in entries_diff:
            f.write('************************************\n')
            f.write(raw_entry.strip() + '\n')


if __name__ == '__main__':
    main()
