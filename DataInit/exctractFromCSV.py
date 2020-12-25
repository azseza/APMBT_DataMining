# -*- coding: utf-8 -*-
import csv
import datetime
import pandas as pd
import os

os.chdir('bulls')
#def CleanData(file, newCsv):
with open('20180103.csv', 'r')as OCsv:
    reader = pd.read_csv(OCsv)
    columns = reader.loc[:, reader.isnull().mean() < .8]
    rows = columns.dropna(axis=0)
    writer = csv.writer(open('test.csv', 'w'), delimiter=',')
    for row in rows:
        writer.writerow(rows)


#CleanData('20180103.csv','newCsv')


