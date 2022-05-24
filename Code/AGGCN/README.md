AGGCN for relation classification
==========

## Preparation

First, download and unzip GloVe vectors:

```
chmod +x download.sh; ./download.sh
```
  
Then open `run_prepare.sh` and uncomment the dataset that you want to prepare. After that run this file.

This will write vocabulary and word vectors as a numpy matrix into the dir `dataset/vocab`.

  

## Training

 
To train open `run_train.sh` and uncomment the model that you want to train. After that run this file.

Model checkpoints and logs will be saved to `./saved_models/01`.
  

## Evaluation

Our pretrained models are located at this link: https://drive.google.com/drive/folders/14ScGdr61YKbKd_wx2C0ZEsx0gsobfdrX?usp=sharing (in folder AGGCN_models)

To run evaluation open `run_eval.sh`, uncomment specific line and run the file. 

## Citation

```
@inproceedings{guo2019aggcn,
 author = {Guo, Zhijiang and Zhang, Yan and Lu, Wei},
 booktitle = {Proc. of ACL},
 title = {Attention Guided Graph Convolutional Networks for Relation Extraction},
 year = {2019}
}
```
