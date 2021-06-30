import csv
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(reader)
    header_row = next(reader)

    for index,column_header in enumerate(header_row):
        print(index,column_header)