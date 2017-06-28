# -*- coding: utf-8 -*-

import csv

with open('input.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = row[2]
        print(date, symbol, closing_price)
        
