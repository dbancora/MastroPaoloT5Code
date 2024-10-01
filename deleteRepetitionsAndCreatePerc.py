import re


def elimina_ripetizioni(file_path):
    """Funzione per filtrare le coppie input-target nel file filtrato e contare le ripetizioni"""
    coppie_uniche = set()  # Per salvare le coppie uniche
    coppie_duplicate_set = set()  # Per salvare le coppie duplicate
    totale_coppie = 0  # Conta tutte le coppie trovate
    coppie_duplicate = 0  # Conta le coppie duplicate

    # Pattern per estrarre input, target e pred
    pattern_input = re.compile(r'\[\+\] input: (.*?)\n', re.DOTALL)
    pattern_target = re.compile(r'\[\*\] target: (.*?)\n', re.DOTALL)
    pattern_pred = re.compile(r'\[-\] pred: (.*?)\n', re.DOTALL)

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        contenuto = file.read()

        # Cerca tutti i blocchi di input, target e pred
        input_matches = pattern_input.findall(contenuto)
        target_matches = pattern_target.findall(contenuto)
        pred_matches = pattern_pred.findall(contenuto)

        # Assicurati che il numero di input, target e pred corrisponda
        if len(input_matches) != len(target_matches) or len(input_matches) != len(pred_matches):
            print("Il numero di input, target e pred non corrisponde!")
            return coppie_uniche, coppie_duplicate_set, totale_coppie, coppie_duplicate

        # Combina input, target e pred in coppie uniche
        for input_value, target_value, pred_value in zip(input_matches, target_matches, pred_matches):
            totale_coppie += 1  # Conta ogni coppia trovata
            coppia = (input_value.strip(), target_value.strip(), pred_value.strip())
            if coppia in coppie_uniche:
                coppie_duplicate += 1  # Incrementa se la coppia è già nel set (duplicata)
                coppie_duplicate_set.add(coppia)  # Aggiungi alla lista delle duplicazioni
            else:
                coppie_uniche.add(coppia)  # Aggiunge la coppia unica

    return coppie_uniche, coppie_duplicate_set, totale_coppie, coppie_duplicate


def salva_file_filtrato(coppie_uniche, output_path):
    """Funzione per salvare le coppie filtrate in un file"""
    with open(output_path, 'w', encoding='utf-8') as file:
        for input_value, target_value, pred_value in coppie_uniche:
            file.write(f"[+] input: {input_value}\n")
            file.write(f"[*] target: {target_value}\n")
            file.write(f"[-] pred: {pred_value}\n")
            file.write("************************************\n")
    print(f"File filtrato salvato in: {output_path}")


def conta_elementi_file_confronto(file_path):
    """Funzione per contare quanti blocchi di predizione ci sono nel file di confronto"""
    blocchi_confronto = []

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        contenuto = file.read()
        # Dividi i blocchi separati da asterischi
        blocchi_confronto = contenuto.split("************************************")
        # Rimuovi blocchi vuoti o spazi bianchi
        blocchi_confronto = [blocco.strip() for blocco in blocchi_confronto if blocco.strip()]

    return blocchi_confronto


def calcola_proporzione(file_filtrato, file_confronto, file_output_filtrato):
    # Ottieni le coppie uniche, il numero di coppie e le ripetizioni nel file filtrato
    coppie_filtrate, coppie_duplicate_set, totale_filtrato, duplicate_filtrato = elimina_ripetizioni(file_filtrato)

    # Salva il file filtrato
    salva_file_filtrato(coppie_filtrate, file_output_filtrato)

    # Ottieni i blocchi dal file di confronto
    blocchi_confronto = conta_elementi_file_confronto(file_confronto)
    totale_confronto = len(blocchi_confronto)  # Numero di blocchi nel file di confronto

    # Conta quanti blocchi del file di confronto hanno una corrispondenza nel file filtrato
    num_coppie_comuni = 0

    # Per ogni blocco del file di confronto, verifichiamo se c'è una coppia corrispondente nel file filtrato
    pattern_input = re.compile(r'\[\+\] input: (.*?)\n', re.DOTALL)
    pattern_target = re.compile(r'\[\*\] target: (.*?)\n', re.DOTALL)

    for blocco in blocchi_confronto:
        input_match = pattern_input.search(blocco)
        target_match = pattern_target.search(blocco)

        if input_match and target_match:
            input_value = input_match.group(1).strip()
            target_value = target_match.group(1).strip()
            # Pred non è usato qui per il confronto
            coppia = (input_value, target_value)

            # Cerca solo input-target nel set delle coppie filtrate
            if any((input_value == coppia_f[0] and target_value == coppia_f[1]) for coppia_f in coppie_filtrate):
                num_coppie_comuni += 1

    # Calcola la proporzione rispetto al file di confronto
    if totale_confronto == 0:
        proporzione = 0.0
    else:
        proporzione = (num_coppie_comuni / totale_confronto) * 100

    # Mostra il risultato
    print(f"Totale coppie trovate nel file filtrato: {totale_filtrato}")
    print(f"Numero di coppie duplicate eliminate: {duplicate_filtrato}")
    print(f"Numero di coppie uniche nel file filtrato: {len(coppie_filtrate)}")
    print(f"Totale blocchi nel file di confronto: {totale_confronto}")
    print(f"Proporzione di blocchi del file di confronto presenti nel file filtrato: {proporzione:.3f}%")

    # Stampa le coppie duplicate
    if coppie_duplicate_set:
        print("\nCoppie duplicate trovate:")
        for input_value, target_value, pred_value in coppie_duplicate_set:
            print(f"[+] input: {input_value}")
            print(f"[*] target: {target_value}")
            print(f"[-] pred: {pred_value}")
            print("************************************")


def main():
    # Specifica il percorso dei file direttamente
    file_filtrato = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/perfect2023_JUnit4_@1.txt'
    file_confronto = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2023_JUnit4_@1.txt'
    file_output_filtrato = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_perfect2023_JUnit4_@1.txt'  # File dove verrà salvato il filtrato

    # Esegui la funzione di calcolo della proporzione
    calcola_proporzione(file_filtrato, file_confronto, file_output_filtrato)


if __name__ == "__main__":
    main()
