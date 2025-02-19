# MastroPaoloT5Code

La seguente repository contiene il codice necessario per utilizzare il modello T5 di MastroPaolo al di fuori dell'ambiente Google Colab. 

Il modello è stato sviluppato da Antonio Mastropaolo e la repository ufficiale è disponibile al seguente link: 

[TransferLearning4Code](https://github.com/antonio-mastropaolo/TransferLearning4Code)

## Istruzioni per il setup

### Download del modello Pytorch

A causa delle limitazioni imposte da GitHub, non è stato possibile caricare il modello PyTorch utilizzato. 
E' necessario quindi scaricarlo tramite il seguente link Google Drive: 

[Modello PyTorch](https://drive.google.com/drive/folders/11nrc1rLbZZViK1TAoqrtmKaKEurVyXGn)

Una volta scaricato, è necessario spostarlo all'interno del path del progetto :

```Trainted-Models/with-pretraining-new/MT-Task-Balanced/Pytorch-Model```

### Setup dell'ambiente 

Il seguente codice è stato sviluppato e testato utilizzando Python 3.10.9 

Inoltre si consiglia di creare un Virtual Enviroment per il download delle librerie necessarie: 

- **nlp** in versione 0.4.0
- **sentencepiece** in versione 0.1.96
- **dill** in versione 0.3.3
- **numpy** in versione 1.26.4
- **torch** in versione 2.4.0
- **transformers** in versione 4.44.2

Una volta installate tutte le librerie, è possibile importare i propri file in formato _.tsv_ affinchè vengano
analizzati dal programma. 

### Specifica del path per i file da analizzare

Per garantire il corretto funzionamento del codice, è necessario specifiare il path del file _.tsv_ da analizzare 
all'interno del file ```main.py``` (situato nella directory principale della repository) oltre che nel file 
```assertion_dataset_script.py``` situato nella cartella _Miscellaneous_ della repository. 

## Test
Il seguente codice è stato testato sia in ambiente Windows che in ambiente Linux (Ubuntu). 

In entrambi i casi, il modello ha terminato l'esecuzione e salvato i risultati nella directory _Result_. 

## Risultati
Questo codice è stato utilizzato per valutare la bontà del modello T5 nel predire parti di codice mancante.
Il modello utilizzato è in grado di sostituire parte del codice di test unitari che viene nascosto. 

I risultati ottenuti sono disponibili [qui](T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/README.md).



