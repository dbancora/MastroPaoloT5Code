# MastroPaoloT5Code

The following repository contains the code needed to use MastroPaolo's T5 model outside the Google Colab environment.

The model was developed by Antonio Mastropaolo and the official repository is available at the following link :

[TransferLearning4Code](https://github.com/antonio-mastropaolo/TransferLearning4Code)

## Setup instructions

### Downloading the Pytorch model

Due to limitations imposed by GitHub, it was not possible to upload the PyTorch model used. 
It is therefore necessary to download it via the following Google Drive link:

[Modello PyTorch](https://drive.google.com/drive/folders/11nrc1rLbZZViK1TAoqrtmKaKEurVyXGn)

Once downloaded, you need to move it within the project path :

```Trainted-Models/with-pretraining-new/MT-Task-Balanced/Pytorch-Model```

### Environment Setup

The following code was developed and tested using Python 3.10.9 

In addition, it is recommended to create a Virtual Enviroment for downloading the necessary libraries: 

- **nlp** in version 0.4.0
- **sentencepiece** in version 0.1.96
- **dill** in version 0.3.3
- **numpy** in version 1.26.4
- **torch** in version 2.4.0
- **transformers** in version 4.44.2

Once you have installed all the libraries, you can import your files in _.tsv_ format for them to be
parsed by the program. 

### Specifying the path for the files to be analyzed

To ensure that the code works properly, it is necessary to specify the path to the _.tsv_ file to be parsed 
within the file ```main.py``` (located in the root directory of the repository) as well as in the  
```assertion_dataset_script.py``` located in the _Miscellaneous_ folder of the repository.

## Test
The following code has been tested in both Windows and Linux (Ubuntu) environments.  

In both cases, the model finished execution and saved the results in the _Result_ directory. 

## Results
This code was used to evaluate the goodness of the T5 model in predicting parts of missing code.
The model used is able to replace part of the unit test code that is hidden.  

The results obtained are available [here](T5-Extension/Results/Predictions/AG-Task/with-pretraining-new/RawWithNoRepetitions/README.md).



