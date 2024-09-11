#Solved
import numpy as np

a = np.zeros(shape=(21,21)) #21x21 Array of zeros

#Put 1's in row&col 1
for x in range(0,21):
    a[0][x] = 1
    a[x][0] = 1

#Put 1,2,3,4... in row&col 2
for x in range(0,21):
    a[1][x] = x+1
    a[x][1] = x+1

for y in range(2,21):
    for x in range(2,21):
        a[y][x] = a[y][x-1] + a[y-1][x]


print(a)

#Too many digits to display in terminal
print(a[20][20] - 137846529000)
#Gives -180, thus
#Answer 137846529000 -180 = 137846528820
