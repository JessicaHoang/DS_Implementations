from hashmaps import *
import csv

import pandas as pd
t = HashTable()

# my implementation
with open('nyc_weather.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, t in enumerate(reader):
        if t['date'] == 'Jan 9':
            print(t['temperature(F)'])
        if t['date'] == 'Jan 4':
            print(t.__getitem__('temperature(F)'))

    


    