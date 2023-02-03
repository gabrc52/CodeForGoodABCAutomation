import csv
from pathlib import Path

filename = 'downloaded/social_explorer/2020.csv'

file = open(filename, "r")
data = list(csv.reader(file, delimiter=","))
file.close()

dictify = {}

#column header
for column_head in data[0]:
    dictify[column_head] = []

#all data points
for row_idx in range(2, len(data)):
    for column_idx in range(len(data[row_idx])):
        dictify[data[0][column_idx]].append(data[row_idx][column_idx])

#removal of null variables
to_del = []
for col in data[0]:
    delete = True
    for datapoint in dictify[col]:
        if datapoint != "":
            delete = False
            continue
    if delete:
        del dictify[col]
        to_del.append(col)

for i in to_del:
    data[0].remove(i)

#removal of 0 variables
to_del = []
for col in data[0]:
    delete = True
    for datapoint in dictify[col]:
        if datapoint != '0':
            delete = False
            continue
    if delete:
        del dictify[col]
        to_del.append(col)

for i in to_del:
    data[0].remove(i)

#removal of dummy variables
dummy_var = ['File identification', 'State Postal Abbreviation', 'Summary Level', 'Geographic Component', 'Logical Record Number', 
             'State (FIPS Code)', 'County of current residence']

for col in dummy_var:
    del dictify[col]
    data[0].remove(col)

print('-------------------   Attributes to look up (quit to exit):   -------------------')
for i in data[0]:
    print(i)


attribute = 'hi :)'
while attribute != 'quit':
    attribute = str(input("Enter attribute: "))
    if attribute != 'quit':
        if attribute not in dictify:
            print('Error Key!')
            continue
        else:
            print(dictify[attribute])