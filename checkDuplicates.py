import re
from collections import defaultdict


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
        # Estrai le linee [+] input e [*] target
        input_line = target_line = ''
        lines = raw_entry.split('\n')
        for line in lines:
            if line.startswith('[+] input:'):
                input_line = line.strip()
            elif line.startswith('[*] target:'):
                target_line = line.strip()
        if input_line and target_line:
            # Aggiungi la coppia input-target alla lista
            entries.append((input_line, target_line))

    return entries


def find_duplicates(entries):
    seen = defaultdict(int)
    duplicates = []

    for entry in entries:
        key = (entry[0], entry[1])
        seen[key] += 1
        if seen[key] > 1:
            duplicates.append(key)

    return duplicates


def main():
    filename = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2020_JUnit4_@10.txt'  # Sostituisci con il percorso del tuo file

    # Parsea le voci dal file
    entries = parse_entries(filename)

    # Conta il numero totale di coppie input-target
    total_entries = len(entries)
    print(f"Numero totale di coppie input-target trovate: {total_entries}")

    # Trova le coppie input-target duplicate
    duplicates = find_duplicates(entries)

    if duplicates:
        print(f"Trovate {len(duplicates)} coppie duplicate:")
        for dup in duplicates:
            print(f"Duplicato: {dup[0]} | {dup[1]}")
    else:
        print("Nessun duplicato trovato.")


if __name__ == '__main__':
    main()

