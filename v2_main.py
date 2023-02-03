import csv
from pathlib import Path
from collections import Counter

csv_path = "downloaded/social_explorer"

class Data_Year:
    def __init__(self, filename):
        self.filename = filename
        self.year = filename[:4]
        self.processed = {}
        self.columns = set()

    def process(self):
        file = open(f"{csv_path}/{self.filename}", "r")
        data = list(csv.reader(file, delimiter=","))
        file.close()

        assert len(data[0]) == len(data[1])

        #column header
        for column_head in range(len(data[0])):
            self.processed[data[1][column_head]] = []

        #all data points
        for row_idx in range(2, len(data)):
            for column_idx in range(len(data[row_idx])):
                self.processed[data[1][column_idx]].append(data[row_idx][column_idx])

        '''
        cols_to_del = set()
        for category in self.processed:
            for datapoint in self.processed[category]:
                if datapoint == '':
                    cols_to_del.add(category)

        for col in cols_to_del:
            del self.processed[col]
            data[0].remove(col)
        '''
        self.columns = set(data[1])
        

    def delete(self, col):
        if col in self.columns:
            self.columns.remove(col)
        if col in self.processed:
            del self.processed[col]

years = ['2021.csv', '2020.csv', '2019.csv', '2018.csv', '2017.csv', '2016.csv', '2015.csv', '2014.csv', '2013.csv', '2012.csv', '2011.csv', '2010.csv', '2009.csv']
save_obj = {}

tmp = Data_Year(years[0]) 
tmp.process()
colliding_categories = tmp.columns
#look at all years and find all similar categories
for year in years:
    tmp = Data_Year(year) 
    tmp.process()
    save_obj[tmp.year] = tmp
    colliding_categories = colliding_categories & tmp.columns

#make all years have the same categories
for year in save_obj:
    to_delete = save_obj[year].columns - colliding_categories
    for deletion in to_delete:
        save_obj[year].delete(deletion)

print('-------------------   Attributes to look up (quit to exit):   -------------------')
for i in colliding_categories:
    print(i)


attribute = 'hi :)'
lookupyear = '0'
try:
    while attribute != 'quit' and lookupyear != 'quit':
        lookupyear = str(input("Enter year: "))
        if lookupyear != 'quit':
            attribute = str(input("Enter attribute: "))
            if attribute != 'quit':
                if attribute not in colliding_categories:
                    print('Error Key!')
                    continue
                else:
                    print(save_obj[lookupyear].processed[attribute])
except EOFError:
    print("\n\nExiting...")
                