# Automatic semantic relation extraction
Aljoša Koren, Klemen Škrlj, Tilen Kavčič and Živa Simonišek

## Abstract
Relation extraction is a task that requires automatic detection and classification of semantic relations within a sentence. In this paper we use deep learning approaches to extract relations from TermFrame dataset, which consists of definitions of Karst specific expressions in English and Slovene. We use BERT and AGGCN models for classification of entity pairs in relation. Our best performing model is RoBERTa with F-score of 75,9\% on English corpus and 73\% on Slovene. Automatic relation extraction performs best for "Definiendum" and "Genus" classes while other relations are quite hard for our model. Lastly we include manual evaluation of automatic extraction and reasoning behind successful and unsuccessful predictions.

### TermFrame dataset:
https://drive.google.com/drive/folders/1CnUIQwtE-81GccO3vwGps_tdbO8ccZPf?usp=sharing
### Pretrained models:
https://drive.google.com/drive/folders/14ScGdr61YKbKd_wx2C0ZEsx0gsobfdrX?usp=sharing