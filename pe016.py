#Solved

x = 2**1000
sum = 0

#Break number into single digits
list = [int(n) for n in str(x)]

print(len(list)) #302

for i in range(0,302):
    sum += list[i]

print(sum)
