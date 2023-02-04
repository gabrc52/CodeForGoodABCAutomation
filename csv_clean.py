import csv
import os
import json
from constants import *
import sys

csv_path = "downloaded/social_explorer"
csv_output_path = "social_explorer_cleaned"

csv_files = [f for f in os.listdir(csv_path) if f.endswith('.csv')]

names = {}

def parse(x: str):
    """
    Attempts to parse the input as an int first. If not successful as a float. If not successful, just returns it

    >>> parse(3.14)
    3.14
    >>> parse(5)
    5
    >>> parse('3.14')
    3.14
    >>> parse('12000000000')
    12000000000
    >>> parse('hello')
    'hello'
    """
    if isinstance(x, str):
        try:
            x = int(x)
        except ValueError:
            try:
                x = float(x)
            except ValueError:
                pass
    return x
    


def clean(sheet: list[list], equivalences=equivalences):
    """
    Cleans up the sheet (list of lists from CSV file). Returns a cleaned up version
    We don't need to worry about mutating `sheet`

    This includes:
    * Removing the first row which has long human-readable names, and instead storing them in a names dictionary
    * Follow the instructions for equivalences in constants.py to replace equivalent properties in the CSV file

    >>> sheet = [ ['Dummy variable a', '_', '_', '_'], ['a','b','c','d'], [1,2,3,4], [2,3,4,5] ]
    >>> clean(sheet, {'b': 'e', 'd': 'e'}) == [ ['a','e','c'], [1,6,3], [2,8,4] ]
    True
    """

    assert len(sheet[0]) == len(sheet[1])
    N = len(sheet[0])
    for i in range(N):
        names[sheet[1][i]] = sheet[0][i]
    sheet.pop(0)

    new_sheet = []

    # Replace based on equivalence dict
    # If we didn't need this, we could simply `return sheet`
    for r in range(1, len(sheet)):
        properties = {}
        for c in range(N):
            property = sheet[0][c]
            if property in equivalences:
                properties.setdefault(equivalences[property], 0)
                properties[equivalences[property]] += parse(sheet[r][c])
            else:
                properties[property] = parse(sheet[r][c])
        if not new_sheet:
            new_sheet.append(list(properties.keys()))
        else:
            # I am (ab)using the fact that when you iterate through a dict,
            # the order of the keys is the insertion order
            assert new_sheet[0] == list(properties.keys())
        new_sheet.append(list(properties.values()))

    return new_sheet

if __name__ == "__main__":
    import doctest
    doctest.testmod()

for filename in csv_files:
    with open(f'{csv_path}/{filename}', 'r') as f:
        sheet = list(csv.reader(f))
    
    sheet = clean(sheet)

    with open(f'{csv_output_path}/{filename}', 'w') as f:
        csv.writer(f).writerows(sheet)

with open('names.json', 'w') as f:
    json.dump(names, f)
