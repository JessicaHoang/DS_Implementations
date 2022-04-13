from re import L
from hashmaps import *
import csv

# object t from HashTable class
t = HashTable()

# Best data structure for this problem?: Hash Table?
# line is current type dictionary. Why?
poem_lines = []
counter = 0
with open('poem.txt', newline="") as f:
    reader = csv.DictReader(f)
    for idx, line in enumerate(f):
        line = line.strip()
        line = line.split(' ')
    #     t[str(idx)] = line
    #     if t[str(idx)] == "\r\n":
    #         print('delete that element from the hash')
    #         t.__delitem__(str(idx))
    # print(t.arr)
        poem_lines.append(line)
        counter += 1
        t[line] = counter
        print(t[line])
    #print(poem_lines)
    # print(t[line])