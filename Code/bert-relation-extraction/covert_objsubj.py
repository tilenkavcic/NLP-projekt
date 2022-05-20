import os
import pandas as pd
import random

DATA_PATH = "../../Data/Annotated Train/EN/TERM_CAT_GEN_SENT_REL.csv"

SEM_EVAL_FILE = "../../Data/Annotated Train/EN/OBJ_SUBJ_FILE_KARST.txt"


df = pd.read_csv(DATA_PATH)
f = open(SEM_EVAL_FILE, "w+", encoding="utf-8")


def write_to_file(f, s, definendium, relation, relation_name, row_index):
    d_index = s.find(definendium)
    if d_index < 0:
        return row_index
    for r in relation:
        r_index = s.find(r)
        s1 = s
        parentheses = "(e1,e2)"
        if r_index < 0:
            continue
        elif d_index < r_index:
            s1 = s1.replace(definendium, "<e1>"+definendium +
                            "</e1>").replace(r, "<e2>"+r+"</e2>")
        else:
            s1 = s1.replace(definendium, "<e2>"+definendium +
                            "</e2>").replace(r, "<e1>"+r+"</e1>")
            parentheses = "(e2,e1)"

        # s1 = s1.encode('ascii',errors='ignore').decode("ascii")

        f.write(str(row_index) + "\t" + "\"" + s1 + "\"\n")
        f.write(relation_name+parentheses+"\n")
        f.write("Comment:\n")
        f.write("\n")
        row_index += 1
    return row_index


row_index = 1
for index, row in df.iterrows():

    genuses = [] if type(row['GENUS']) == float or len(
        row['GENUS']) <= 0 else row['GENUS'].split("|")
    definendium = row['DEFINIENDUM']
    sentence = row['SENTENCE']
    locations = [] if type(row['HAS_LOCATION']) == float or len(
        row['HAS_LOCATION']) <= 0 else row['HAS_LOCATION'].split("|")
    forms = [] if type(row['HAS_FORM']) == float or len(
        row['HAS_FORM']) <= 0 else row['HAS_FORM'].split("|")
    cause = [] if type(row['HAS_CAUSE']) == float or len(
        row['HAS_CAUSE']) <= 0 else row['HAS_CAUSE'].split("|")
    comp = [] if type(row['COMPOSITION_MEDIUM']) == float or len(
        row['COMPOSITION_MEDIUM']) <= 0 else row['COMPOSITION_MEDIUM'].split("|")
    sizes = [] if type(row['HAS_SIZE']) == float or len(
        row['HAS_SIZE']) <= 0 else row['HAS_SIZE'].split("|")
    functions = [] if type(row['HAS_FUNCTION']) == float or len(
        row['HAS_FUNCTION']) <= 0 else row['HAS_FUNCTION'].split("|")

    row_index = write_to_file(f, sentence, definendium,
                              genuses, "Genus", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              forms, "Has_form", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              locations, "Has_location", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              cause, "Has_cause", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              comp, "Composition_medium", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              sizes, "Has_size", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              functions, "Has_function", row_index)


pre_picked = set(['GENUS', 'HAS_FORM', 'HAS_LOCATION', 'HAS_CAUSE', 'COMPOSITION_MEDIUM', 'HAS_SIZE', 'HAS_FUNCTION', "DEFINITOR"])
new = set(df.columns[df.columns.get_loc("AFFECTS"):df.columns.get_loc("STUDIES")+1])
new -= pre_picked

counter = 0
df_shuffled = df.sample(frac=1, random_state=1).reset_index(drop=True)
for index, row in df_shuffled.iterrows():
    columns = row[row.notna()]
    curr_inter = new.intersection(set(columns.keys()))
    for relation in curr_inter:
        definendium = row['DEFINIENDUM']
        sentence = row['SENTENCE']
        relations = [] if type(row[relation]) == float or len(
            row[relation]) <= 0 else row[relation].split("|")
        
        row_index =  write_to_file(f, sentence, definendium,
                    relations, "Other", row_index)
        counter += len(relations)
    
    if counter > 200:
        break

counter = 0
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
for index, row in df_shuffled.iterrows():
    sentence = row['SENTENCE']
    definendium = row['DEFINIENDUM']
    temp_sent = sentence.replace(definendium, "")
    tokens = temp_sent.split(" ")
    num_tokens = len(tokens)
    start = random.randint(0, num_tokens-5)
    length = random.randint(1,5)
    try:
        rand_relation = " ".join(tokens[start:start+length])
        if len(rand_relation) == 0 or rand_relation== ":" or rand_relation==".":
            continue

        rand_relations = [rand_relation]
        row_index = write_to_file(f, sentence, definendium,
                rand_relations, "Other", row_index)
        counter += 1
    except:
        print("Invalid random relation")

    if counter > 100:
        break

f.close()


