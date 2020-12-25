'''
Convert PDF to CSVtable
@uthor hichembenh
collecting all links
'''


# -*- coding: utf-8 -*-

import datetime
import os
import pandas as pd
import tabula


def ConvertPDFtoXLSX(pdf,newXLSX):
    try:
        df = tabula.read_pdf(pdf, pages=1)
        df = pd.concat(df)
        df.to_excel(newXLSX)
        print(newXLSX + ' converted')
        os.remove(pdf)
        print(pdf+' deleted')
    except:
        print( pdf+' not found')
def ExtractFromCSV(newXLSX):
    try:
        reader = pd.read_excel(newXLSX, header=None)
        columns = reader.loc[17:88, reader.isnull().mean() < .8]
        columns.to_excel(newXLSX)
        newReader = pd.read_excel(newXLSX, header=None)
        newColumns = newReader.loc[1:49, 6:10]
        os.remove(newXLSX)
        newColumns.to_excel(newXLSX)
        print (newXLSX+' fitred')
    except:
        print(newXLSX+' not found')

for i in range(1000):
    date = datetime.date(2018, 1, 1)
    date += datetime.timedelta(i)
    anne = date.year
    mois = date.month
    jour = date.day
    anne = str(anne)
    if jour < 10:
        jour = str(jour)
        jour = '0' + jour
    if mois < 10:
        mois = str(mois)
        mois = '0' + mois

    jour = str(jour)
    mois = str(mois)
    assert (type(anne) == str and type(mois) == str and type(jour) == str)
    pdf = 'bull' + anne + mois + jour + '.pdf'
    newXLSX = anne + mois + jour + '.xlsx'
    ConvertPDFtoXLSX(pdf,newXLSX)
    ExtractFromCSV(newXLSX)

