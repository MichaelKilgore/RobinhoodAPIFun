#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re

#i>AHC</a></td><td><a href="
#grep the 'AHC' of the above line



url = 'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies='
urladdon = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0']

for k in urladdon:

	r = requests.get(url + k)
	print(url + k)

	match = re.findall(r'[A-Z]{1,4}</a></td><td><a href=', r.text)
	stocks = []
	if len(match)>0:
		for m in match:
			stocks.append(re.sub(r'</a></td><td><a href=', '', m))
		
	mylist = list(dict.fromkeys(stocks))
	print(mylist)

	with open('Companies.txt', 'a') as f:
    		for item in mylist:
		        f.write("%s\n" % item)

