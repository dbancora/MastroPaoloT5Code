# Questo script elimina le ripetizioni all'interno dei file
import re
from collections import Counter

def extract_triplets(file_path):
    """
    Estrae tutte le triplette (input, target, pred) da un file.

    Args:
        file_path (str): Il percorso del file di input.

    Returns:
        list of tuples: Una lista di triplette estratte come tuple (input, target, pred).
    """
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()

    # Espressione regolare per identificare triplette
    triplet_pattern = re.compile(
        r'\[\+\] input:\s*(.*?)\n\[\*\] target:\s*(.*?)\n\[-\] pred:\s*(.*?)(?=\n\[\+\] input:|\Z)',
        re.DOTALL
    )

    triplets = triplet_pattern.findall(content)

    # Debug: Stampa le prime 5 triplette estratte
    print(f"Triplette estratte dal file {file_path}:")
    for i, triplet in enumerate(triplets[:5], start=1):
        print(f"Triplette {i}:")
        print(f"Input:\n{triplet[0].strip()}")
        print(f"Target:\n{triplet[1].strip()}")
        print(f"Pred:\n{triplet[2].strip()}")
        print("-" * 50)
    print(f"Totale triplette estratte: {len(triplets)}\n")

    return triplets

def elimina_ripetizioni(file_path, output_path):
    """
    Elimina le triplette duplicate basate su (input, target) e salva le triplette uniche nel file di output.
    Inoltre, stampa il numero di coppie estratte e segnala se ci sono duplicazioni.

    Args:
        file_path (str): Il percorso del file di input.
        output_path (str): Il percorso del file di output.
    """
    # Estrai tutte le triplette
    triplets = extract_triplets(file_path)

    # Crea una lista di coppie (input, target)
    pairs = [(input_val.strip(), target_val.strip()) for input_val, target_val, pred_val in triplets]

    # Conta le occorrenze di ogni coppia
    counter = Counter(pairs)

    # Identifica le coppie duplicate
    duplicates = [(pair, count) for pair, count in counter.items() if count > 1]

    # Stampa il numero di coppie estratte
    total_pairs = len(pairs)
    unique_pairs = len(counter)
    duplicate_pairs_count = sum(count - 1 for pair, count in duplicates)

    print(f"Numero totale di coppie (input, target) estratte: {total_pairs}")
    print(f"Numero di coppie uniche: {unique_pairs}")
    if duplicates:
        print(f"Numero di coppie duplicate: {len(duplicates)}")
        print("Esempi di coppie duplicate:")
        for pair, count in duplicates[:5]:  # Mostra solo i primi 5 duplicati
            print(f"({pair[0]}, {pair[1]}) - {count} occorrenze")
    else:
        print("Nessuna coppia duplicata trovata.")
    print()

    # Filtra le triplette uniche basate su (input, target)
    coppie_uniche = set()
    contenuto_filtrato = []
    coppie_duplicate_rimosse = 0

    for triplet_num, (input_val, target_val, pred_val) in enumerate(triplets, start=1):
        coppia = (input_val.strip(), target_val.strip())
        if coppia not in coppie_uniche:
            coppie_uniche.add(coppia)
            # Rimuovi eventuali asterischi residui e linee vuote
            input_clean = re.sub(r'\*{36,}', '', input_val.strip())
            target_clean = re.sub(r'\*{36,}', '', target_val.strip())
            pred_clean = re.sub(r'\*{36,}', '', pred_val.strip())
            blocco = f"[+] input: {input_clean}\n[*] target: {target_clean}\n[-] pred: {pred_clean}"
            contenuto_filtrato.append(blocco)
        else:
            coppie_duplicate_rimosse += 1

    # Definisci il separatore come una sola linea di asterischi
    separatore = "\n************************************\n************************************\n"

    # Scrivi il contenuto filtrato nel file di output senza linee vuote aggiuntive
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for i, blocco in enumerate(contenuto_filtrato):
            output_file.write(blocco)
            if i < len(contenuto_filtrato) - 1:
                output_file.write(separatore)

    # Stampa i risultati finali
    print(f"Totale triplette trovate nel file originale: {len(triplets)}")
    print(f"Numero di triplette duplicate rimosse: {coppie_duplicate_rimosse}")
    print(f"Numero di triplette uniche salvate nel file di output: {len(coppie_uniche)}")
    print(f"Filtraggio completato. Risultato salvato in {output_path}\n")

def main():
    """
    Funzione principale per eseguire lo script di filtraggio delle triplette.
    """
    # Specifica i percorsi del file di input e di output
    input_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/perfect2024_JUnit5_OneAssert_@10.txt'
    output_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_perfect2024_JUnit5_OneAssert_@10.txt'

    # Esegui la funzione di filtraggio
    elimina_ripetizioni(input_file, output_file)

if __name__ == "__main__":
    main()

#Inzia con 2024