x = 1
for i in range(1, 101):
    x *= i
    
sum = 0
for digit in str(x):
    sum += int(digit)

print(sum)