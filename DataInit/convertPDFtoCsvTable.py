'''
Convert PDF to CSV
@uthor hichembenh
collecting all links
'''


# -*- coding: utf-8 -*-

import datetime
import tabula

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
    pdf='bull'+ anne + mois + jour + '.pdf'
    newCsv= anne + mois + jour + '.csv'
    try:
      tabula.convert_into(pdf,newCsv,output_format='csv',pages=1)
      print(newCsv+' converti')
    except:
        print( pdf+' non trouvé')