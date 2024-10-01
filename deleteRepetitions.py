import re


def elimina_ripetizioni(file_path, output_path):
    # Dizionario per tenere traccia delle coppie uniche di input e target
    coppie_uniche = set()
    coppie_duplicate = 0
    totale_coppie = 0

    # Pattern per estrarre input e target
    pattern_input = re.compile(r'\[\+\] input: (.*?)\n', re.DOTALL)
    pattern_target = re.compile(r'\[\*\] target: (.*?)\n', re.DOTALL)

    # Lista per salvare il contenuto filtrato
    contenuto_filtrato = []

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        contenuto = file.read()

        # Dividi il contenuto nei blocchi separati da "************************************"
        blocchi = contenuto.split("************************************")

        for blocco in blocchi:
            # Cerca input e target nel blocco
            input_match = pattern_input.search(blocco)
            target_match = pattern_target.search(blocco)

            if input_match and target_match:
                totale_coppie += 1  # Conta ogni coppia trovata
                input_value = input_match.group(1).strip()
                target_value = target_match.group(1).strip()

                # Crea una coppia unica
                coppia = (input_value, target_value)

                # Se la coppia non è già stata aggiunta, aggiungila alla lista e set
                if coppia not in coppie_uniche:
                    coppie_uniche.add(coppia)
                    contenuto_filtrato.append(blocco)
                else:
                    coppie_duplicate += 1  # Conta le coppie duplicate

    # Scrivi il contenuto filtrato nel file di output
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("************************************".join(contenuto_filtrato))

    # Stampa i risultati
    print(f"Totale coppie trovate nel file originale: {totale_coppie}")
    print(f"Numero di coppie duplicate rimosse: {coppie_duplicate}")
    print(f"Numero di coppie uniche salvate nel file di output: {len(coppie_uniche)}")
    print(f"Filtraggio completato. Risultato salvato in {output_path}")

def main():
    # Qui specifichi i percorsi del file di input e di output direttamente
    input_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/Raw/prediction_2024_JUnit5_@10.txt'
    output_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2024_JUnit5_@10.txt'

    # Esegui la funzione di filtraggio
    elimina_ripetizioni(input_file, output_file)

if __name__ == "__main__":
    main()
