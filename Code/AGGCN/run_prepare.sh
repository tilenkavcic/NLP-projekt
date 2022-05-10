#!/bin/bash


# For semeval dataset
# python3 prepare_vocab.py dataset/semeval dataset/vocab --glove_dir dataset/glove

# For karst dataset
python3 prepare_vocab.py dataset/karst dataset/vocab_karst --glove_dir dataset/glove

