#Solved
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for div in range(3,sqr,2):
        if n % div == 0:
            return False
    return True

count = 1 #to include 2 (as we start at 1 and the increment 2)
for x in range(1,100000000000,2):
    if is_prime(x):
        count += 1
    if count == 10001:
        print(x)
        exit()
