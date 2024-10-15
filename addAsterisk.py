def add_asterisk_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    new_lines = []
    add_initial_asterisks = True  # Flag per aggiungere asterischi all'inizio

    if add_initial_asterisks:
        new_lines.append('************************************\n')

    for line in lines:
        new_lines.append(line)
        if line.strip() == '************************************':
            # Aggiungi una linea di asterischi dopo ogni linea di asterischi
            new_lines.append('************************************\n')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(new_lines)

def main():
    # Specifica i nomi dei file di input e output
    input_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2020_JUnit4_@10.txt'   # Sostituisci con il nome del tuo file di input
    output_file = 'T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/NOREP_prediction_2020_JUnit4_WithAsterisk_@10.txt'  # Sostituisci con il nome del file di output desiderato

    # Chiama la funzione per aggiungere le linee di asterischi
    add_asterisk_lines(input_file, output_file)
    print(f"Processamento completato. Il file modificato è stato salvato come '{output_file}'.")

if __name__ == '__main__':
    main()
