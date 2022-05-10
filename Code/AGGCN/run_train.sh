#!/bin/bash

# For semeval dataset
# CUDA_VISIBLE_DEVICES=0  python3 train.py  --save_dir ./saved_models_semeval --id 1 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2 --pooling_l2 0.002

# For Karst dataset
CUDA_VISIBLE_DEVICES=1  python3 train.py --data_dir dataset/karst --vocab_dir dataset/vocab_karst --save_dir ./saved_models_karst --batch_size 32 --id 1 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2 --pooling_l2 0.002

