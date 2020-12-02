import requests
import datetime
import os 
import socket
url = 'http://www.tse.tn/sites/default/files/bulletin/pdf/bull'
for i in range(1000):
    date = datetime.date(2018,1,1)
    date += datetime.timedelta(i)
    anne = date.year
    mois = date.month
    jour = date.day
    anne=str(anne)
    if jour < 10 :
        jour =str(jour)
        jour ='0'+jour
    if mois < 10 : 
        mois = str(mois)
        mois = '0'+mois
     
    jour = str(jour)
    mois = str(mois)
    
    assert(type(anne) == str and type(mois) == str and type(jour) == str )
    furl = url+anne+mois+jour+'.pdf'
    bulll = 'bull'+anne+mois+jour+'.pdf'
    a = requests.head(furl)
    print('requesting '+furl)
    if a.status_code==200 : 
        files = requests.get(furl)
        with open(bulll,'wb') as f : 
            f.write(files.content)
        f.close()

    else :
        print('404 error for' + anne +'-'+mois+'-'+jour)
    
