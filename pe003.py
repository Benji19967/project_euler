#Solved
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

sqrt = int(math.sqrt(600851475143))

for x in range (1,sqrt,1):
    if 600851475143 % x == 0 and is_prime(x):
        y = x

print(y)
