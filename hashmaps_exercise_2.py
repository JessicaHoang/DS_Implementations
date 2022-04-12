from hashmaps import *
import time
import csv

t = HashTable()
start_time = time.time()

# my implementation
# utilizes hashtable
with open('nyc_weather.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, t in enumerate(reader):
        if t['date'] == 'Jan 9':
            print(t['temperature(F)'])
        if t['date'] == 'Jan 4':
            print(t.__getitem__('temperature(F)'))
print("--- %s seconds ---" % (time.time() - start_time)) # mine is faster

# their implementation
# utilizes dictionary
weather_dict = {}
with open("nyc_weather.csv", 'r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature. ignore the row")

print(weather_dict['Jan 4'])
print(weather_dict['Jan 9'])
print("--- %s seconds ---" % (time.time() - start_time))


    