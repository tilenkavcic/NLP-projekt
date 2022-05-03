import os
import pandas as pd
import json
import re

DATA_PATH = "../data/Annotated/EN/TERM_CAT_GEN_SENT_REL.csv"
# SEM_EVAL_FILE = "../HRL-RE-master/data/Karst/test.json"
SEM_EVAL_TRAIN = "../HRL-RE-master/data/Karst/test.json"
SEM_EVAL_TEST = "../HRL-RE-master/data/Karst/train.json"

df = pd.read_csv(DATA_PATH)


def get_relations(d_index, definendium, genuses, relations, sentence, type):
    for r in genuses:
        relation = {}
        r_index = sentence.find(r)
        if r_index < 0:
            continue

        relation["rtext"] = type
        # relation["rtext"] = "/location/location/contains"

        d_i = 0 if d_index == 0 else len(sentence[:d_index - 1].split(" "))
        r_i = 0 if r_index == 0 else len(sentence[:r_index - 1].split(" "))

        tags = [0] * len(sentence.split(" "))

        if d_index < r_index:
            relation["em2"] = definendium
            relation["em1"] = r

            tags[r_i] = 4
            for i in range(1, len(r.split(" "))):
                tags[r_i + i] = 1

            tags[d_i] = 5
            for i in range(1, len(definendium.split(" "))):
                tags[d_i + i] = 2
        else:
            relation["em2"] = r
            relation["em1"] = definendium

            tags[d_i] = 4
            for i in range(1, len(definendium.split(" "))):
                tags[d_i + i] = 1

            tags[r_i] = 5
            for i in range(1, len(r.split(" "))):
                tags[r_i + i] = 2




        relation["tags"] = tags
        relations.append(relation)


def makeJson(sentence, definendium, genuses, locations, sizes):
    dat = {}
    sentence = re.sub('([.,!?()])', r' \1 ', sentence)
    sentence = re.sub('\s{2,}', ' ', sentence)
    if sentence[-1] == " ":
        sentence = sentence[:-1]
    d_index = sentence.find(definendium)
    if d_index < 0:
        return None
    dat["sentext"] = sentence
    ent = genuses + locations + sizes
    ent.append(definendium)
    dat["entities"] = ent

    relations = []
    get_relations(d_index, definendium, genuses, relations, sentence, "genus")
    get_relations(d_index, definendium, locations, relations, sentence, "location")
    get_relations(d_index, definendium, sizes, relations, sentence, "size")

    if relations == []:
        return None
    else:
        dat["relations"] = relations
        return dat


if __name__ == '__main__':
    num_train = df.shape[0] * 0.8

    with open(SEM_EVAL_TRAIN, 'w') as train_f, open(SEM_EVAL_TEST, "w") as test_f:
        for index, row in df.iterrows():
            genuses = [] if type(row['GENUS']) == float or len(
                row['GENUS']) <= 0 else row['GENUS'].split("|")
            definendium = row['DEFINIENDUM']
            sentence = row['SENTENCE']
            locations = [] if type(row['HAS_LOCATION']) == float or len(
                row['HAS_LOCATION']) <= 0 else row['HAS_LOCATION'].split("|")
            sizes = [] if type(row['HAS_SIZE']) == float or len(
                row['HAS_SIZE']) <= 0 else row['HAS_SIZE'].split("|")

            compiled_json = makeJson(sentence, definendium, genuses, locations, sizes)

            if compiled_json != None:
                if index < num_train:
                    json.dump(compiled_json, train_f)
                    train_f.write("\n")
                else:
                    json.dump(compiled_json, test_f)
                    test_f.write("\n")
