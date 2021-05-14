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

### **Audio files in opus format**

| Archive          | Size       |  Link           |
|------------------|------------|-----------------|
| golos_opus.tar   | 20.5 GB    | https://  |

---

### **Audio files in wav format**

| Archives          | Size       |  Links          |
|-------------------|------------|-----------------|
| train_farfield.tar| 15.4 GB    | https://  |
| train_crowd0.tar  | 11 GB      | https://  |
| train_crowd1.tar  | 14 GB      | https://  |
| train_crowd2.tar  | 13.2 GB    | https://  |
| train_crowd3.tar  | 11.6 GB    | https://  |
| train_crowd4.tar  | 15.8 GB    | https://  |
| train_crowd5.tar  | 13.1 GB    | https://  |
| train_crowd6.tar  | 15.7 GB    | https://  |
| train_crowd7.tar  | 12.7 GB    | https://  |
| train_crowd8.tar  | 12.2 GB    | https://  |
| train_crowd9.tar  | 8.08 GB    | https://  |
| test.tar          | 1.3 GB     | https://  |

---

### **Acoustic and language models**

Acoustic model QuartzNet15x5

Three n-gram language models (KenLM)
- Built on CommonCrawl dataset
- Built on Golos dataset
- Built on CommonCrawl and Golos datasets together (50/50)

| Archives                 | Size       |  Links          |
|--------------------------|------------|-----------------|
| QuartzNet15x5_golos.nemo | 68 MB      | https://  |
| KenLMs.tar               | 4.8 GB     | https://  |

## **License**

[Similar to CC Attribution ShareAlike](https://sberbank.ru/licenses/by-sa/3.0)

## **Contacts**

Please create a GitHub issue!

Authors (in alphabetic order):
- Alexander Denisenko
- Fedor Minkin
- Nikolay Karpov
