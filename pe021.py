amics = {} # example {"220": 284, "284": 220}
all_amics = set()
total = 0
for i in range(1, 10000):
    propers = []
    for div in range(1, i):
        if(i % div == 0):
            propers.append(div)
    
    sum = 0
    for x in propers:
        sum += x

    if(sum in amics):
        if(amics[sum] == i):
            all_amics.add(i)
            all_amics.add(sum)
    else:
        amics[i] = sum

for y in all_amics:
    print(y)
    total += y

print(total)