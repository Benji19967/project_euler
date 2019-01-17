#Solved
import csv
import numpy as np

with open('pe11.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=' ')

    list = []
    for row in readCSV:
        for x in range(0,20):
            row[x] = int(row[x])
        list.append(row)

    array = np.asarray(list) #Convert a list into an array

print(list)
print(type(list))
print(array)
print(type(array))
print(array[0][0])
print(type(array[0][0]))
#At this point my data is nicely ordered in an Array like I want it

prod = 0
#Largest product 4 numbers in a ROW
for i in range(0,20):
    for j in range(0,16):
        x = array[i][j]*array[i][j+1]*array[i][j+2]*array[i][j+3]
        if x > prod:
            prod = x

#Largest product 4 numbers in a COLUMN
for j in range(0,20):
    for i in range(0,16):
        x = array[i][j]*array[i+1][j]*array[i+2][j]*array[i+3][j]
        if x > prod:
            prod = x

#Largest product 4 numbers diagonally down
for i in range(0,16):
    for j in range(0,16):
        x = array[i][j]*array[i+1][j+1]*array[i+2][j+2]*array[i+3][j+3]
        if x > prod:
            prod = x

#Largest product 4 numbers diagonally up (WINNER!)
for i in range(0,16):
    for j in range(3,20):
        x = array[i][j]*array[i+1][j-1]*array[i+2][j-2]*array[i+3][j-3]
        if x > prod:
            prod = x
print(prod)
