#!/bin/bash

# For semeval dataset
# CUDA_VISIBLE_DEVICES=0  python3 train.py  --save_dir ./saved_models_semeval --id 1 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2 --pooling_l2 0.002

# For Karst dataset all
# CUDA_VISIBLE_DEVICES=1  python3 train.py --data_dir dataset/karst_all --vocab_dir dataset/vocab_karst_all --save_dir ./saved_models_karst --id 1 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2

# For Karst dataset picked
# CUDA_VISIBLE_DEVICES=1  python3 train.py --data_dir dataset/karst --vocab_dir dataset/vocab_karst --save_dir ./saved_models_karst --id 2 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2

# For Karst slo dataset all
# CUDA_VISIBLE_DEVICES=1  python3 train.py --data_dir dataset/karst_sl_all --vocab_dir dataset/vocab_karst_sl_all --save_dir ./saved_models_karst_sl --id 1 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2

# For Karst slo dataset picked
CUDA_VISIBLE_DEVICES=1  python3 train.py --data_dir dataset/karst_sl --vocab_dir dataset/vocab_karst_sl --save_dir ./saved_models_karst_sl --id 2 --seed 1 --hidden_dim 360 --lr 0.5 --rnn_hidden 300 --num_epoch 150 --pooling max  --mlp_layers 1 --num_layers 2


