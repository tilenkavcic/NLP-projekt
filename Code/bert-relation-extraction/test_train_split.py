import random

SEM_EVAL_FILE = "./Data/Annotated/EN/SEM_EVAL_FILE_KARST.txt"

SEM_EVAL_FILE_TRAIN = "./Data/Annotated/EN/SEM_EVAL_FILE_KARST_TRAIN.txt"

SEM_EVAL_FILE_TEST = "./Data/Annotated/EN/SEM_EVAL_FILE_KARST_TEST.txt"

f_train = open(SEM_EVAL_FILE_TRAIN, "w")
f_test = open(SEM_EVAL_FILE_TEST, "w")

N = 4

a = list(range(1, 2041))
train_len = int(0.7*len(a))
sample = random.sample(a, train_len)

index_train = 1
index_test = train_len+1

row_now = 1
with open(SEM_EVAL_FILE, 'r') as infile:
    count = 0
    for line_idx, line in enumerate(infile):
        #lines = [line for line in infile][:N]
        if line_idx % 4 == 0:
            c = line.split("\t")[1:]
            c = "\t".join(c)
            cc = ""
            if row_now in sample:
                cc = str(index_train) + "\t" + c
                f_train.write(cc)
                index_train += 1
            else:
                cc = str(index_test) + "\t" + c
                f_test.write(cc)
                index_test += 1
        else:
            if row_now in sample:
                f_train.write(line)
            else:
                f_test.write(line)
        count += 1
        if count == 4:
            count = 0
            row_now += 1

f_train.close()
f_test.close()
