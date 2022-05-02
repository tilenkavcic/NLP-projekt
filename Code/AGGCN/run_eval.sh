#!/bin/bash

# For semeval dataset
# CUDA_VISIBLE_DEVICES=0 python3 eval.py saved_models_semeval/01 --dataset test --data_dir dataset/semeval > results/results_semeval.txt

# For Karst dataset
CUDA_VISIBLE_DEVICES=1 python3 eval.py saved_models_karst/01 --dataset test --data_dir dataset/karst > results/results_karst.txt
