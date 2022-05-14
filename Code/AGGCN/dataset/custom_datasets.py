import json

picked = ['GENUS', 'HAS_FORM', 'HAS_LOCATION', 'HAS_CAUSE', 'COMPOSITION_MEDIUM', 'HAS_SIZE', 'HAS_FUNCTION','GENUS_rev', 'HAS_FORM_rev', 'HAS_LOCATION_rev', 'HAS_CAUSE_rev', 'COMPOSITION_MEDIUM_rev', 'HAS_SIZE_rev', 'HAS_FUNCTION_rev']

f = open("./karst_sl_all/train.json")
data = json.load(f)
f.close()

picked_data = []

for d in data:
    if d["relation"] in picked:
        picked_data.append(d)

print("Picked lines", len(picked_data))

json_data = json.dumps(picked_data, indent=4)

with open("./karst_sl/train.json", "w+") as outfile:
    outfile.write(json_data)
