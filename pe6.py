#Solved
sum1 = 0
sum2 = 0

for x in range(1,101):
    sum1 += x**2

for y in range(1,101):
    sum2 += y
sum2 = sum2**2

ans = sum2 - sum1
print(ans)
