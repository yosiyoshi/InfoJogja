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
r = requests.get(target_url)         #get contents with requests
stname = re.sub('https://id.wikipedia.org/wiki/', '', str(target_url))
soup = BeautifulSoup(r.text, 'lxml') #use beautifulsoup
time = str(now.hour) + "."
output = soup.find_all("td", text=re.compile(time))      #fist to find trains on time
output2 = re.sub('[</td>]', '', str(output))
output3 = output2.replace(".", ":")
t = "Bisnis"
c = soup.find_all("td", text=re.compile(t))
c2 = re.sub('[(</td>);]', '', str(c))
c3 = re.sub('amp', '', c2)
print("Timetable at " + stname + ":\n" + output3 + "\nYou want to take " + t + " class train; \nAvailable trains stopping at " + stname + " per a day are:\n" + c3)
