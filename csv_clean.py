import csv
import os
import json
import constants

csv_path = "downloaded/social_explorer"
csv_output_path = "social_explorer_cleaned"

csv_files = [f for f in os.listdir(csv_path) if f.endswith('.csv')]

names = {}

def clean(sheet: list[list]):
    assert len(sheet[0]) == len(sheet[1])
    N = len(sheet[0])
    for i in range(N):
        names[sheet[1][i]] = sheet[0][i]
    sheet.pop(0)
    # TODO: implement replacing based on `equivalences` in `constants.py`

for filename in csv_files:
    with open(f'{csv_path}/{filename}', 'r') as f:
        sheet = list(csv.reader(f))
    
    clean(sheet)

    with open(f'{csv_output_path}/{filename}', 'w') as f:
        csv.writer(f).writerows(sheet)

with open('names.json', 'w') as f:
    json.dump(names, f)
