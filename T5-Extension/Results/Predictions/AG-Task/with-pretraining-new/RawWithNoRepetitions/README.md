# Risultati ottenuti
Nelle seguenti tabelle sono riportati i risultati ottenuti dal modello T5 nel compito di Assert generation (AG) con l'utilizzo di codice "grezzo". 
<!--
## Repository create nell'anno 2020
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI   |
|------|----------------------|----------------|-----------|------------|----------------------|-------------------------------------------|
| 2020 | 19792                | 4              | 1         | 12         | 2,890                | 572                                       |
| 2020 | 19792                | 4              | 5         | 12         | 5,502                | 1089                                      |
| 2020 | 19792                | 4              | 10        | 12         | 6,447                | 1276                                      |
| 2020 | 22960                | 5              | 1         | 12         | 2,657                | 610                                       |
| 2020 | 22960                | 5              | 5         | 12         | 4,713                | 1082                                      |
| 2020 | 22960                | 5              | 10        | 12         | 5,357                | 1230                                      |

## Repository create nell'anno 2021
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 11053                | 4              | 1         | 12         | 4,542                | 502                                     |
| 2021 | 11053                | 4              | 5         | 12         | 7,817                | 864                                     |
| 2021 | 11053                | 4              | 10        | 12         | 9,020                | 997                                     |
| 2021 | 16844                | 5              | 1         | 12         | 1,989                | 335                                     |
| 2021 | 16844                | 5              | 5         | 12         | 4,114                | 693                                     |
| 2021 | 16844                | 5              | 10        | 12         | 4,773                | 804                                     |

## Repository create nell'anno 2022
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 17011                | 4              | 1         | 12         | 2,163                | 368                                     |
| 2022 | 17011                | 4              | 5         | 12         | 4,103                | 698                                     |
| 2022 | 17011                | 4              | 10        | 12         | 4,679                | 796                                     |
| 2022 | 14377                | 5              | 1         | 12         | 3.770                | 542                                     |
| 2022 | 14377                | 5              | 5         | 12         | 6,691                | 962                                     |
| 2022 | 14377                | 5              | 10        | 12         | 7,679                | 1104                                    |


## Repository create nell'anno 2023
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2023 | 14452                | 4              | 1         | 12         | 5,044                | 729                                     |
| 2023 | 14452                | 4              | 5         | 12         | 10,587               | 1530                                    |
| 2023 | 14452                | 4              | 10        | 12         | 11,569               | 1672                                    |
| 2023 | 11526                | 5              | 1         | 12         | 4,407                | 508                                     |
| 2023 | 11526                | 5              | 5         | 12         | 7,435                | 857                                     |
| 2023 | 11526                | 5              | 10        | 12         | 8,598                | 991                                     |

## Repository create nell'anno 2024
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 363                  | 4              | 1         | 12         | 3,857                | 14                                      |
| 2024 | 363                  | 4              | 5         | 12         | 5,510                | 20                                      |
| 2024 | 363                  | 4              | 10        | 12         | 6,887                | 25                                      |
| 2024 | 1201                 | 5              | 1         | 12         | 4,163                | 50                                      |
| 2024 | 1201                 | 5              | 5         | 12         | 9,159                | 110                                     |
| 2024 | 1201                 | 5              | 10        | 12         | 11,407               | 137                                     |

## Repository create nell'anno 2020 con una sola asserzione
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 8332                 | 4              | 1         | 12         | 4,081                | 340                                     |
| 2020 | 8332                 | 4              | 5         | 12         | 6,781                | 565                                     |
| 2020 | 8332                 | 4              | 10        | 12         | 7,885                | 657                                     |
| 2020 | 11731                | 5              | 1         | 12         | 3,785                | 444                                     |
| 2020 | 11731                | 5              | 5         | 12         | 6,001                | 704                                     |
| 2020 | 11731                | 5              | 10        | 12         | 6,530                | 766                                     |

## Repository create nell'anno 2021 con una sola asserzione
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 4820                 | 4              | 1         | 12         | 7,282                | 351                                     |
| 2021 | 4820                 | 4              | 5         | 12         | 11,826               | 570                                     |
| 2021 | 4820                 | 4              | 10        | 12         | 13,444               | 648                                     |
| 2021 | 9638                 | 5              | 1         | 12         | 2,283                | 220                                     |
| 2021 | 9638                 | 5              | 5         | 12         | 4,389                | 423                                     |
| 2021 | 9638                 | 5              | 10        | 12         | 4,970                | 479                                     |

## Repository create nell'anno 2022 con una sola asserzione
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 8390                 | 4              | 1         | 12         | 2,765                | 232                                     |
| 2022 | 8390                 | 4              | 5         | 12         | 4,529                | 380                                     |
| 2022 | 8390                 | 4              | 10        | 12         | 4,887                | 410                                     |
| 2022 | 7846                 | 5              | 1         | 12         | 5,175                | 406                                     |
| 2022 | 7846                 | 5              | 5         | 12         | 8,246                | 647                                     |
| 2022 | 7846                 | 5              | 10        | 12         | 9,317                | 731                                     |

## Repository create nell'anno 2023 con una sola asserzione
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2023 | 6919                 | 4              | 1         | 12         | 9,134                | 632                                     |
| 2023 | 6919                 | 4              | 5         | 12         | 17,965               | 1243                                    |
| 2023 | 6919                 | 4              | 10        | 12         | 18,948               | 1311                                    |
| 2023 | 5107                 | 5              | 1         | 12         | 7,323                | 374                                     |
| 2023 | 5107                 | 5              | 5         | 12         | 11,396               | 582                                     |
| 2023 | 5107                 | 5              | 10        | 12         | 12,473               | 637                                     |

## Repository create nell'anno 2024 con una sola asserzione
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 184                  | 4              | 1         | 12         | 7,609                | 14                                      |
| 2024 | 184                  | 4              | 5         | 12         | 9,783                | 18                                      |
| 2024 | 184                  | 4              | 10        | 12         | 11,957               | 22                                      |
| 2024 | 454                  | 5              | 1         | 12         | 7,930                | 36                                      |
| 2024 | 454                  | 5              | 5         | 12         | 16,960               | 77                                      |
| 2024 | 454                  | 5              | 10        | 12         | 20,264               | 92                                      |
-->
# Senza distinzione versione JUnit
## Senza distinzione di anno
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| All  | 127953               | 4 & 5          | 1         | 12         | 3,291                | 4211                                    |
| All  | 127953               | 4 & 5          | 5         | 12         | 6,130                | 7844                                    |
| All  | 127953               | 4 & 5          | 10        | 12         | 7,003                | 8960                                    |

## Repository create nell'anno 2020 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 41856                | 4 & 5          | 1         | 12         | 2,807                | 1175                                    |
| 2020 | 41856                | 4 & 5          | 5         | 12         | 5,120                | 2143                                    |
| 2020 | 41856                | 4 & 5          | 10        | 12         | 5,911                | 2474                                    |

## Repository create nell'anno 2021 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 27750                | 4 & 5          | 1         | 12         | 3,016                | 837                                     |
| 2021 | 27750                | 4 & 5          | 5         | 12         | 5,593                | 1552                                    |
| 2021 | 27750                | 4 & 5          | 10        | 12         | 6,454                | 1791                                    |

## Repository create nell'anno 2022 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 30981                | 4 & 5          | 1         | 12         | 2,924                | 906                                     |
| 2022 | 30981                | 4 & 5          | 5         | 12         | 5,319                | 1648                                    |
| 2022 | 30981                | 4 & 5          | 10        | 12         | 6,097                | 1889                                    |

## Repository create nell'anno 2023 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2023 | 25837                | 4 & 5          | 1         | 12         | 4,768                | 1232                                    |
| 2023 | 25837                | 4 & 5          | 5         | 12         | 9,204                | 2378                                    |
| 2023 | 25837                | 4 & 5          | 10        | 12         | 10,268               | 2653                                    |

## Repository create nell'anno 2024 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 1529                 | 4 & 5          | 1         | 12         | 4,003                | 61                                      |
| 2024 | 1529                 | 4 & 5          | 5         | 12         | 8,071                | 123                                     |
| 2024 | 1529                 | 4 & 5          | 10        | 12         | 10,039               | 153                                     |

# Con distinzione versione JUnit
## Repository create nell'anno 2020 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 19338                | 4              | 1         | 12         | 2,948                | 570                                     |  
| 2020 | 19338                | 4              | 5         | 12         | 5,600                | 1082                                    | 
| 2020 | 19338                | 4              | 10        | 12         | 6,557                | 1268                                    | 
| 2020 | 22518                | 5              | 1         | 12         | 2,687                | 605                                     | 
| 2020 | 22518                | 5              | 5         | 12         | 4,712                | 1061                                    | 
| 2020 | 22518                | 5              | 10        | 12         | 5,356                | 1206                                    | 

## Repository create nell'anno 2021 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 10971                | 4              | 1         | 12         | 4,576                | 502                                     |  
| 2021 | 10971                | 4              | 5         | 12         | 7,830                | 859                                     | 
| 2021 | 10971                | 4              | 10        | 12         | 9,006                | 988                                | 
| 2021 | 16779                | 5              | 1         | 12         | 1,997                | 335                                     |  
| 2021 | 16779                | 5              | 5         | 12         | 4,130                | 693                                     | 
| 2021 | 16779                | 5              | 10        | 12         | 4,786                | 803                                     | 

## Repository create nell'anno 2022 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 16775                | 4              | 1         | 12         | 2,176                | 365                                     |  
| 2022 | 16775                | 4              | 5         | 12         | 4,119                | 691                                     |  
| 2022 | 16775                | 4              | 10        | 12         | 4,703                | 789                                     |   
| 2022 | 14206                | 5              | 1         | 12         | 3,808                | 541                                     | 
| 2022 | 14206                | 5              | 5         | 12         | 6,737                | 957                                     | 
| 2022 | 14206                | 5              | 10        | 12         | 7,743                | 1100                                    | 


## Repository create nell'anno 2023 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2023 | 14387                | 4              | 1         | 12         | 5,053                | 727                                     |  
| 2023 | 14387                | 4              | 5         | 12         | 10,607               | 1526                                    |    
| 2023 | 14387                | 4              | 10        | 12         | 11,587               | 1667                                    | 
| 2023 | 11450                | 5              | 1         | 12         | 4.410                | 505                                     | 
| 2023 | 11450                | 5              | 5         | 12         | 7,441                | 852                                     | 
| 2023 | 11450                | 5              | 10        | 12         | 8,611                | 986                                     | 

## Repository create nell'anno 2024 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 363                  | 4              | 1         | 12         | 3,857                | 14                                      |  
| 2024 | 363                  | 4              | 5         | 12         | 5,510                | 20                                      | 
| 2024 | 363                  | 4              | 10        | 12         | 6,887                | 25                                      | 
| 2024 | 1166                 | 5              | 1         | 12         | 4,031                | 47                                      | 
| 2024 | 1166                 | 5              | 5         | 12         | 8,834                | 103                                     | 
| 2024 | 1166                 | 5              | 10        | 12         | 10,978               | 128                                     | 


## Repository create nell'anno 2020 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 8167                 | 4              | 1         | 12         | 4,139                | 338                                     |   
| 2020 | 8167                 | 4              | 5         | 12         | 6,881                | 562                                     | 
| 2020 | 8167                 | 4              | 10        | 12         | 7,996                | 653                                     | 
| 2020 | 11475                | 5              | 1         | 12         | 3,834                | 440                                     | 
| 2020 | 11475                | 5              | 5         | 12         | 6,022                | 691                                     | 
| 2020 | 11475                | 5              | 10        | 12         | 6,536                | 750                                     | 

## Repository create nell'anno 2021 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 4777                 | 4              | 1         | 12         | 7,348                | 351                                     |  
| 2021 | 4777                 | 4              | 5         | 12         | 11,911               | 569                                     |  
| 2021 | 4777                 | 4              | 10        | 12         | 13,502               | 645                                     | 
| 2021 | 9598                 | 5              | 1         | 12         | 2,292                | 220                                     | 
| 2021 | 9598                 | 5              | 5         | 12         | 4,407                | 423                                     | 
| 2021 | 9598                 | 5              | 10        | 12         | 4,991                | 479                                     | 

## Repository create nell'anno 2022 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 8219                 | 4              | 1         | 12         | 2,823                | 232                                     | 
| 2022 | 8219                 | 4              | 5         | 12         | 4,599                | 378                                     | 
| 2022 | 8219                 | 4              | 10        | 12         | 4,964                | 408                                     | 
| 2022 | 7746                 | 5              | 1         | 12         | 5,229                | 405                                     | 
| 2022 | 7746                 | 5              | 5         | 12         | 8,314                | 644                                     | 
| 2022 | 7746                 | 5              | 10        | 12         | 9,411                | 729                                     | 

## Repository create nell'anno 2023 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE  | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|-------------|----------------------|-----------------------------------------|
| 2023 | 6885                 | 4              | 1         | 12          | 9,165                | 631                                     | 
| 2023 | 6885                 | 4              | 5         | 12          | 18,025               | 1241                                    | 
| 2023 | 6885                 | 4              | 10        | 12          | 19,012               | 1309                                    | 
| 2023 | 5080                 | 5              | 1         | 12          | 7,323                | 372                                     | 
| 2023 | 5080                 | 5              | 5         | 12          | 11,398               | 579                                     | 
| 2023 | 5080                 | 5              | 10        | 12          | 12,480               | 634                                     | 

## Repository create nell'anno 2024 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 184                  | 4              | 1         | 12         | 7,609                | 14                                      | 
| 2024 | 184                  | 4              | 5         | 12         | 9,783                | 18                                      | 
| 2024 | 184                  | 4              | 10        | 12         | 11,957               | 22                                      | 
| 2024 | 434                  | 5              | 1         | 12         | 7,604                | 33                                      | 
| 2024 | 434                  | 5              | 5         | 12         | 16,129               | 70                                      | 
| 2024 | 434                  | 5              | 10        | 12         | 19,124               | 83                                      | 

## Repository create nell'anno 2020 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 11171                | 4              | 1         | 12         | 2,077                | 232                                     | 
| 2020 | 11171                | 4              | 5         | 12         | 4,655                | 520                                     |  
| 2020 | 11171                | 4              | 10        | 12         | 5,505                | 615                                     | 
| 2020 | 11043                | 5              | 1         | 12         | 1,494                | 165                                     | 
| 2020 | 11043                | 5              | 5         | 12         | 3,351                | 370                                     |  
| 2020 | 11043                | 5              | 10        | 12         | 4,129                | 456                                     | 

## Repository create nell'anno 2021 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 6194                 | 4              | 1         | 12         | 2,438                | 151                                     | 
| 2021 | 6194                 | 4              | 5         | 12         | 4,682                | 290                                     | 
| 2021 | 6194                 | 4              | 10        | 12         | 5,538                | 343                                     | 
| 2021 | 7181                 | 5              | 1         | 12         | 1,601                | 115                                     | 
| 2021 | 7181                 | 5              | 5         | 12         | 3,760                | 270                                     | 
| 2021 | 7181                 | 5              | 10        | 12         | 4,512                | 324                                     | 

## Repository create nell'anno 2022 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 8556                 | 4              | 1         | 12         | 1,554                | 133                                     |   
| 2022 | 8556                 | 4              | 5         | 12         | 3,658                | 313                                     | 
| 2022 | 8556                 | 4              | 10        | 12         | 4,453                | 381                                     | 
| 2022 | 6460                 | 5              | 1         | 12         | 2,105                | 136                                     | 
| 2022 | 6460                 | 5              | 5         | 12         | 4,845                | 313                                     | 
| 2022 | 6460                 | 5              | 10        | 12         | 5,743                | 371                                     | 

## Repository create nell'anno 2023 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE  | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|-------------|----------------------|-----------------------------------------|
| 2023 | 7502                 | 4              | 1         | 12          | 1,280                | 96                                      | 
| 2023 | 7502                 | 4              | 5         | 12          | 3,799                | 285                                     | 
| 2023 | 7502                 | 4              | 10        | 12          | 4,772                | 358                                     | 
| 2023 | 6370                 | 5              | 1         | 12          | 2,088                | 133                                     | 
| 2023 | 6370                 | 5              | 5         | 12          | 4,286                | 273                                     | 
| 2023 | 6370                 | 5              | 10        | 12          | 5,526                | 352                                     | 

## Repository create nell'anno 2024 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 179                  | 4              | 1         | 12         | 0,000                | 0                                       |    
| 2024 | 179                  | 4              | 5         | 12         | 1,117                | 2                                       | 
| 2024 | 179                  | 4              | 10        | 12         | 1,676                | 3                                       | 
| 2024 | 732                  | 5              | 1         | 12         | 1,913                | 14                                      | 
| 2024 | 732                  | 5              | 5         | 12         | 4,508                | 33                                      | 
| 2024 | 732                  | 5              | 10        | 12         | 6,148                | 45                                      | 
