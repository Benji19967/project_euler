# Solved

x = 2**1000
sum = 0

# Break number into single digits
digits = [int(n) for n in str(x)]

print(len(digits))  # 302

for i in range(0, 302):
    sum += digits[i]

print(sum)
