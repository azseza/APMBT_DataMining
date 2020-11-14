'''
Data downloader from http://www.bvmt.com.tn/fr/content/historique-des-donn%C3%A9es
@uthor AzsezA
collecting all links
'''
import requests
from bs4 import BeautifulSoup
import wget
import re
import csv
site= 'http://www.bvmt.com.tn/fr/content/historique-des-donn%C3%A9es'
#Testing the links
def isDow(url:str):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if content_type == None :
        return True
    elif 'text' in content_type.lower():
        return False
    else :
        return True
#Searching for links in bvmt
print('requesting : '+site +' ...')
resp = requests.get(site)
soup = BeautifulSoup(resp.text, 'html')
print('prasing all links')
divid = soup.find_all('a', string=True)
print('printing output in links.csv : ' )
with open('links.csv', 'w', newline='') as csvfile:
    header = ['Dirty link','Clean link','Is it Downloadble']
    writer = csv.DictWriter(csvfile,fieldnames = header)
    writer.writeheader()
    for link in divid:
        a = link.get('href')
        print('doing this link : '+a)
        b = 'http://www.bvmt.com.tn'+link.get('href')
        if type(b) != None:
            print(type(b))
            print('link'+a)
            c = isDow(b)
        else :
            c = None
        writer.writerow({'Dirty link': a,
            'Clean link': b,
            'Is it Downloadble': c})
print("done")
