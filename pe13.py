#Solved
import csv
import numpy as np
from itertools import chain

with open('pe13.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\n')

    numbers = []
    for row in readCSV:
        numbers.append(row)

numbers[0][0] = int(numbers[0][0]) #We have a nested list

#Extracting nested list
numbers = list(chain.from_iterable(numbers))

#Convert list of str to int
for x in range(0,100):
    numbers[x] = int(numbers[x])

#print(numbers)
#print((numbers[0]))

sum = 0
for x in range(0,100):
    sum += numbers[x]

print(sum)
