# Golos dataset

Golos is a Russian corpus suitable for speech research. The dataset mainly consists of recorded audio files manually annotated on the crowd-sourcing platform. The total duration of the audio is about 1240 hours. 
We have made the corpus freely available for downloading, along with the acoustic model prepared on this corpus. 
Also we create 3-gram KenLM language model using an open Common Crawl corpus.

# Table of contents

- [Dataset structure](https://github.com/sberdevices/golos/#dataset-structure)
- [Downloads](https://github.com/sberdevices/golos/#downloads)
  - [Audio files in opus format](https://github.com/sberdevices/golos/#audio-files-in-opus-format)
  - [Audio files in wav format](https://github.com/sberdevices/golos/#audio-files-in-wav-format)
  - [Acoustic and language models](https://github.com/sberdevices/golos/#acoustic-and-language-models)
- [Evaluation](https://github.com/sberdevices/golos/#evaluation)
- [License](https://github.com/sberdevices/golos/#license)
- [Contacts](https://github.com/sberdevices/golos/#contacts)


## **Dataset structure**

| Domain         | Train files | Train hours  | Test files | Test hours |
|----------------|------------|--------|-------|------|
| Crowd          | 979 796    | 1 095  | 9 994 | 11.2 |
| Farfield       | 124 003    |   132.4| 1 916 |  1.4 |
| Total          | 1 103 799  | 1 227.4|11 910 | 12.6 |

---

## **Downloads**

[MD5 Checksums](https://github.com/sberdevices/golos/blob/master/md5sum.txt)


### **Audio files in opus format**

| Archive          | Size       |  Link               |
|------------------|------------|---------------------|
| golos_opus.tar   | 20.5 GB    | https://sc.link/JpD |

---

### **Audio files in wav format**

| Archives          | Size       |  Links              |
|-------------------|------------|---------------------|
| train_farfield.tar| 15.4 GB    | https://sc.link/1Z3 |
| train_crowd0.tar  | 11 GB      | https://sc.link/Lrg |
| train_crowd1.tar  | 14 GB      | https://sc.link/MvQ |
| train_crowd2.tar  | 13.2 GB    | https://sc.link/NwL |
| train_crowd3.tar  | 11.6 GB    | https://sc.link/Oxg |
| train_crowd4.tar  | 15.8 GB    | https://sc.link/Pyz |
| train_crowd5.tar  | 13.1 GB    | https://sc.link/Qz7 |
| train_crowd6.tar  | 15.7 GB    | https://sc.link/RAL |
| train_crowd7.tar  | 12.7 GB    | https://sc.link/VG5 |
| train_crowd8.tar  | 12.2 GB    | https://sc.link/WJW |
| train_crowd9.tar  | 8.08 GB    | https://sc.link/XKk |
| test.tar          | 1.3 GB     | https://sc.link/Kqr |

---

### **Acoustic and language models**

Acoustic model built using [QuartzNet15x5](https://arxiv.org/pdf/1910.10261.pdf) architecture and trained using [NeMo toolkit](https://github.com/NVIDIA/NeMo/tree/r1.0.0b4)


Three n-gram language models created using [KenLM Language Model Toolkit](https://kheafield.com/code/kenlm)

* LM built on [Common Crawl](https://commoncrawl.org) Russian dataset
* LM built on [Golos](https://github.com/sberdevices/golos) train set
* LM built on [Common Crawl](https://commoncrawl.org) and [Golos](https://github.com/sberdevices/golos) datasets together (50/50)

| Archives                 | Size       |  Links          |
|--------------------------|------------|-----------------|
| QuartzNet15x5_golos.nemo | 68 MB      | https://sc.link/ZMv |
| KenLMs.tar               | 4.8 GB     | https://sc.link/YL0  |


Golos data and models are also available in the hub of pre-trained models, datasets, and containers - DataHub ML Space. You can train the model and deploy it on the high-performance SberCloud infrastructure in [ML Space](https://sbercloud.ru/ru/aicloud/mlspace) - full-cycle machine learning development platform for DS-teams collaboration based on the Christofari Supercomputer.


## **Evaluation**

Percents of Word Error Rate for different test sets


| Decoder \ Test set    | Crowd test  | Farfield test    | MCV<sup>1</sup> dev | MCV<sup>1</sup> test |
|-------------------------------------|-----------|----------|-----------|----------|
| Greedy decoder                      | 4.389 %   | 14.949 % | 9.314 %   | 11.278 % |
| Beam Search with Common Crawl LM    | 4.709 %   | 12.503 % | 6.341 %   | 7.976 % |
| Beam Search with Golos train set LM | 3.548 %   | 12.384 % |  -        | -       |
| Beam Search with Common Crawl and Golos LM | 3.318 %   | 11.488 % | 6.4 %     | 8.06 %   |


<sup>1</sup> [Common Voice](https://commonvoice.mozilla.org) - Mozilla's initiative to help teach machines how real people speak.

## **License**

[English Version](https://github.com/sberdevices/golos/blob/master/license/en_us.pdf)

[Russian Version](https://github.com/sberdevices/golos/blob/master/license/ru.pdf)

## **Contacts**

Please create a GitHub issue!

Authors (in alphabetic order):
- Alexander Denisenko
- Fedor Minkin
- Nikolay Karpov
