#!/bin/bash

# For semeval dataset
# CUDA_VISIBLE_DEVICES=0 python3 eval.py saved_models_semeval/01 --dataset test --data_dir dataset/semeval > results/results_semeval.txt

# For Karst dataset all
# CUDA_VISIBLE_DEVICES=1 python3 eval.py saved_models_karst/01 --dataset test --data_dir dataset/karst_all > results/results_karst_all.txt

# For Karst dataset picked
# CUDA_VISIBLE_DEVICES=1 python3 eval.py saved_models_karst/02 --dataset test --data_dir dataset/karst > results/results_karst.txt

# For Karst dataset all
# CUDA_VISIBLE_DEVICES=1 python3 eval.py saved_models_karst_sl/01 --dataset test --data_dir dataset/karst_sl_all > results/results_karst_sl_all.txt

# For Karst dataset picked
CUDA_VISIBLE_DEVICES=1 python3 eval.py saved_models_karst_sl/02 --dataset test --data_dir dataset/karst_sl > results/results_karst_sl.txt
