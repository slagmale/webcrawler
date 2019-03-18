import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

import pandas  as pd

df = pd.read_csv('data.csv')
print(df)