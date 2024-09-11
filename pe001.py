#Solved (benji19967)
sum = 0
for x in range(1,1000):
    if(x % 3 == 0):
        sum += x
        continue
    if(x % 5 == 0):
        sum += x
print(sum)
