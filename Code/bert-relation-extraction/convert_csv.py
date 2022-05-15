import os
import pandas as pd

DATA_PATH = "./Data/Annotated Train/SL/TERM_CAT_GEN_SENT_REL.csv"

SEM_EVAL_FILE = "./Data/Annotated Train/SL/SEM_EVAL_FILE_KARST.txt"


df = pd.read_csv(DATA_PATH)
f = open(SEM_EVAL_FILE, "w")


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
        f.write(str(row_index) + "\t" + "\"" + s1 + "\"\n")
        f.write(relation_name+parentheses+"\n")
        f.write("Comment:\n")
        f.write("\n")
        row_index += 1
    return row_index


row_index = 1
for index, row in df.iterrows():

    definendium = row['DEFINIENDUM']
    sentence = row['SENTENCE']

    genuses = [] if type(row['GENUS']) == float or len(
        row['GENUS']) <= 0 else row['GENUS'].split("|")
    locations = [] if type(row['HAS_LOCATION']) == float or len(
        row['HAS_LOCATION']) <= 0 else row['HAS_LOCATION'].split("|")
    sizes = [] if type(row['HAS_SIZE']) == float or len(
        row['HAS_SIZE']) <= 0 else row['HAS_SIZE'].split("|")

    forms = [] if type(row['HAS_FORM']) == float or len(
        row['HAS_FORM']) <= 0 else row['HAS_FORM'].split("|")
    functions = [] if type(row['HAS_FUNCTION']) == float or len(
        row['HAS_FUNCTION']) <= 0 else row['HAS_FUNCTION'].split("|")
    cause = [] if type(row['HAS_CAUSE']) == float or len(
        row['HAS_CAUSE']) <= 0 else row['HAS_CAUSE'].split("|")

    composition_medium = [] if type(row['COMPOSITION_MEDIUM']) == float or len(
        row['COMPOSITION_MEDIUM']) <= 0 else row['COMPOSITION_MEDIUM'].split("|")

    row_index = write_to_file(f, sentence, definendium,
                              genuses, "Genus", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              locations, "Has_location", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              sizes, "Has_size", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              forms, "Has_form", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              functions, "Has_function", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              cause, "Has_cause", row_index)
    row_index = write_to_file(f, sentence, definendium,
                              composition_medium, "Composition_medium", row_index)

f.close()
