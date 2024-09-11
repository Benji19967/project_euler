#Solved
sum = 0
count = 1
num = 2
while num <= 4000000:
    if num % 2 == 0:
        sum += num
    x = num
    num = num + count
    count = x
print(sum)
