#Solved
import math

sum = 0
div = 0
for x in range (1,100000000000):
    sum += x

    sqr = int(math.sqrt(sum))+1

    for y in range(1,sqr):
        if sum % y == 0:
            div += 1
            print(sum, div)
            if div == 250:
                print(sum)
                exit()

    div = 0
