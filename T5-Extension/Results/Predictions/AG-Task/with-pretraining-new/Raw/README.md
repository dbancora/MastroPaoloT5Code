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
## Repository create nell'anno 2020 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 8046                 | 4              | 1         | 12         | 4,188                | 337                                     |
| 2020 | 8046                 | 4              | 5         | 12         | 6,972                | 561                                     |
| 2020 | 8046                 | 4              | 10        | 12         | 8,103                | 652                                     |
| 2020 | 11408                | 5              | 1         | 12         | 3,857                | 440                                     |
| 2020 | 11408                | 5              | 5         | 12         | 6,013                | 686                                     |
| 2020 | 11408                | 5              | 10        | 12         | 6,522                | 744                                     |

## Repository create nell'anno 2021 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 4759                 | 4              | 1         | 12         | 7,333                | 349                                     |
| 2021 | 4759                 | 4              | 5         | 12         | 11,914               | 567                                     |
| 2021 | 4759                 | 4              | 10        | 12         | 13,511               | 643                                     |
| 2021 | 9582                 | 5              | 1         | 12         | 2,296                | 220                                     |
| 2021 | 9582                 | 5              | 5         | 12         | 4,415                | 423                                     |
| 2021 | 9582                 | 5              | 10        | 12         | 4,999                | 479                                     |

## Repository create nell'anno 2022 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 8129                 | 4              | 1         | 12         | 2,829                | 230                                     |
| 2022 | 8129                 | 4              | 5         | 12         | 4,589                | 373                                     |
| 2022 | 8129                 | 4              | 10        | 12         | 4,945                | 402                                     |
| 2022 | 7645                 | 5              | 1         | 12         | 5,154                | 394                                     |
| 2022 | 7645                 | 5              | 5         | 12         | 8,241                | 630                                     |
| 2022 | 7645                 | 5              | 10        | 12         | 9,339                | 714                                     |

## Repository create nell'anno 2023 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE  | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|-------------|----------------------|-----------------------------------------|
| 2023 | 6856                 | 4              | 1         | 12          | 9,189                | 630                                     |
| 2023 | 6856                 | 4              | 5         | 12          | 18,086               | 1240                                    |
| 2023 | 6856                 | 4              | 10        | 12          | 19,078               | 1308                                    |
| 2023 | 5054                 | 5              | 1         | 12          | 7,341                | 371                                     |
| 2023 | 5054                 | 5              | 5         | 12          | 11,397               | 576                                     |
| 2023 | 5054                 | 5              | 10        | 12          | 12,465               | 630                                     |

## Repository create nell'anno 2024 con una sola asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 184                  | 4              | 1         | 12         | 7,609                | 14                                      |
| 2024 | 184                  | 4              | 5         | 12         | 9,783                | 18                                      |
| 2024 | 184                  | 4              | 10        | 12         | 11,957               | 22                                      |
| 2024 | 431                  | 5              | 1         | 12         | 7,657                | 33                                      |
| 2024 | 431                  | 5              | 5         | 12         | 16,241               | 70                                      |
| 2024 | 431                  | 5              | 10        | 12         | 19,258               | 83                                      |

## Repository create nell'anno 2020 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 11080                | 4              | 1         | 12         | 2,094                | 232                                     |
| 2020 | 11080                | 4              | 5         | 12         | 4,693                | 520                                     |
| 2020 | 11080                | 4              | 10        | 12         | 5,551                | 615                                     |
| 2020 | 10995                | 5              | 1         | 12         | 1,501                | 165                                     |
| 2020 | 10995                | 5              | 5         | 12         | 3,356                | 369                                     |
| 2020 | 10995                | 5              | 10        | 12         | 4,138                | 455                                     |

## Repository create nell'anno 2021 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 6181                 | 4              | 1         | 12         | 2,443                | 151                                     |
| 2021 | 6181                 | 4              | 5         | 12         | 4,692                | 290                                     |
| 2021 | 6181                 | 4              | 10        | 12         |                      |                                         |
| 2021 | 7172                 | 5              | 1         | 12         | 1,861                | 115                                     |
| 2021 | 7172                 | 5              | 5         | 12         | 4,368                | 270                                     |
| 2021 | 7172                 | 5              | 10        | 12         | 5,242                | 324                                     |

## Repository create nell'anno 2022 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 8494                 | 4              | 1         | 12         | 1,542                | 131                                     |
| 2022 | 8494                 | 4              | 5         | 12         | 3,638                | 309                                     |
| 2022 | 8494                 | 4              | 10        | 12         | 4,427                | 376                                     |
| 2022 | 6450                 | 5              | 1         | 12         | 2,109                | 136                                     |
| 2022 | 6450                 | 5              | 5         | 12         | 4,853                | 313                                     |
| 2022 | 6450                 | 5              | 10        | 12         | 5,752                | 371                                     |

## Repository create nell'anno 2023 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE  | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|-------------|----------------------|-----------------------------------------|
| 2023 | 7481                 | 4              | 1         | 12          | 1,283                | 96                                      |
| 2023 | 7481                 | 4              | 5         | 12          | 3,796                | 284                                     |
| 2023 | 7481                 | 4              | 10        | 12          | 4,772                | 357                                     |
| 2023 | 6365                 | 5              | 1         | 12          | 2,090                | 133                                     |
| 2023 | 6365                 | 5              | 5         | 12          | 4,289                | 273                                     |
| 2023 | 6365                 | 5              | 10        | 12          | 5,530                | 352                                     |

## Repository create nell'anno 2024 multi asserzione senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 179                  | 4              | 1         | 12         | 0,000                | 0                                       |
| 2024 | 179                  | 4              | 5         | 12         | 1,117                | 2                                       |
| 2024 | 179                  | 4              | 10        | 12         | 1,676                | 3                                       |
| 2024 | 730                  | 5              | 1         | 12         | 1,918                | 14                                      |
| 2024 | 730                  | 5              | 5         | 12         | 4,521                | 33                                      |
| 2024 | 730                  | 5              | 10        | 12         | 6,164                | 45                                      |

## Repository create nell'anno 2020 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2020 | 19126                | 4              | 1         | 12         | 2,975                | 569                                     |
| 2020 | 19126                | 4              | 5         | 12         | 5,652                | 1081                                    |
| 2020 | 19126                | 4              | 10        | 12         | 6,624                | 1267                                    |
| 2020 | 22403                | 5              | 1         | 12         | 2,701                | 605                                     |
| 2020 | 22403                | 5              | 5         | 12         | 4,709                | 1055                                    |
| 2020 | 22403                | 5              | 10        | 12         | 5,352                | 1199                                    |

## Repository create nell'anno 2021 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2021 | 10940                | 4              | 1         | 12         | 4,570                | 500                                     |
| 2021 | 10940                | 4              | 5         | 12         | 7,834                | 857                                     |
| 2021 | 10940                | 4              | 10        | 12         | 5,319                | 988                                     |
| 2021 | 16754                | 5              | 1         | 12         | 2,000                | 335                                     |
| 2021 | 16754                | 5              | 5         | 12         | 4,136                | 693                                     |
| 2021 | 16754                | 5              | 10        | 12         | 4,793                | 803                                     |

## Repository create nell'anno 2022 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2022 | 16623                | 4              | 1         | 12         | 2,172                | 361                                     |
| 2022 | 16623                | 4              | 5         | 12         | 4,103                | 682                                     |
| 2022 | 16623                | 4              | 10        | 12         | 4,680                | 778                                     |
| 2022 | 14095                | 5              | 1         | 12         | 3,760                | 530                                     |
| 2022 | 14095                | 5              | 5         | 12         | 6,690                | 943                                     |
| 2022 | 14095                | 5              | 10        | 12         | 7,698                | 1085                                    |


## Repository create nell'anno 2023 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2023 | 14337                | 4              | 1         | 12         | 5,064                | 726                                     |
| 2023 | 14337                | 4              | 5         | 12         | 10,630               | 1524                                    |
| 2023 | 14337                | 4              | 10        | 12         | 11,613               | 1665                                    |
| 2023 | 11419                | 5              | 1         | 12         | 4.414                | 504                                     |
| 2023 | 11419                | 5              | 5         | 12         | 7,435                | 849                                     |
| 2023 | 11419                | 5              | 10        | 12         | 8,600                | 982                                     |

## Repository create nell'anno 2024 senza ripetizioni
| ANNO | NUMERO METODI TOTALI | VERSIONE JUNIT | BEAM SIZE | BATCH SIZE | % PERFECT PREDICTION | NUMERO DI PLACEHOLDER CORRETTI PREDETTI |
|------|----------------------|----------------|-----------|------------|----------------------|-----------------------------------------|
| 2024 | 363                  | 4              | 1         | 12         | 3,857                | 14                                      |
| 2024 | 363                  | 4              | 5         | 12         | 5,510                | 20                                      |
| 2024 | 363                  | 4              | 10        | 12         | 6,887                | 25                                      |
| 2024 | 1161                 | 5              | 1         | 12         | 4,048                | 47                                      |
| 2024 | 1161                 | 5              | 5         | 12         | 8,872                | 103                                     |
| 2024 | 1161                 | 5              | 10        | 12         | 11,025               | 128                                     |
