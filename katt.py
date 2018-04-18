# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:36:50 2018

@author: Yosiyoshi
"""
import datetime
import requests
import re
from collections import Counter

from bs4 import BeautifulSoup

now = datetime.datetime.now()
target_url = 'https://id.wikipedia.org/wiki/Stasiun_Yogyakarta'
r = requests.get(target_url)         #requestsを使って、webから取得
stname = re.sub('https://id.wikipedia.org/wiki/', '', str(target_url))
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
time = str(now.hour) + "."
output = soup.find_all("td", text=re.compile(time))      #リンクを表示
output2 = re.sub('[</td>]', '', str(output))
output3 = output2.replace(".", ":")
t = "Ekonomi"
c = soup.find_all("td", text=re.compile(t))
c2a = re.sub('[(</=>);]', '', str(c))
c2b = re.sub('td', '', c2a)
c3 = re.sub('amp', '', c2b)
c4 = re.sub('href', '', c3)
c5 = re.sub('ile', '', c4)
print("Timetable at " + stname + ":\n" + output3 + "\nYou want to take " + t + " class train; \nAvailable trains stopping at " + stname + " per a day are:\n" + c5)
