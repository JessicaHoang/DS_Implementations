'''
HashTable Exercise 1
'''
import csv
from hashmaps import *

t = HashTable()
# reading csv file
with open('nyc_weather.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sum = 0
    avg = 0
    max = 0
    # iterating through to get the 7 day's temperatures and take the average of it:
    for idx, t in enumerate(reader):
        if int(t['temperature(F)']) > max:
            max = int(t['temperature(F)'])
        if idx < 7:
            sum += int(t['temperature(F)'])
    avg = sum/7
    avg = int(avg)
    print("The average is: ", avg, " degrees F")
    print("The max: ", max)
