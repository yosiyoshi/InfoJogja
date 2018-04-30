"""
Created on Mon Apr 30 16:30:19 2018

@author: yosiyoshi
"""
import requests as web
import bs4
import csv
import collections
soup = bs4.BeautifulSoup(resp.text, "html.parser")

list_keywd = ['toko','baik','jogja']
resp = web.get('https://www.google.co.jp/search?num=100&q=' + '　'.join(list_keywd))
resp.raise_for_status()

scr = soup.select('.s > .st')
for i in range(len(scr)):
    t01 = scr[i].get_text()
    t02 = t01.replace('\n','')
    t03 = t02.replace('\r','')
    t04 = t03.replace('[(/^.,!:;?^\)]','')
    t05 = t04.replace('<span', '')
    t06 = t05.replace('class="st">', '')
    t07 = t06.replace('<br>', '')
    t08 = t07.replace('<b>', '')
    t09 = t08.lower()
bid =  t09.split(" ")
print(bid)
c = collections.Counter(bid)
print(c.most_common(10))
