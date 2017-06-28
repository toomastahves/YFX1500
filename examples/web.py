# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from time import sleep

base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="
books = []
NUM_PAGES = 31

for page_num in range(1, NUM_PAGES + 1):
    print(page_num, " ", len(books))
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    for td in soup('td', 'thumbtext'):
        books.append(td)
    
    sleep(30)
    