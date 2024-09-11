#Solved
import math

for a in range(1,1000):
    for b in range(a,1000):
        c_sqd = a*a + b*b
        if math.sqrt(c_sqd) % 1 == 0:
            if a + b + math.sqrt(c_sqd) == 1000:
                print(a)
                print(b)
                print(math.sqrt(c_sqd))
                print(a * b * math.sqrt(c_sqd))
                exit()
