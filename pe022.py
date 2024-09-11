f = open("pe22_names.txt", "r")
for line in f:
    currentline = line.split(",")

names = [i.replace('"', '') for i in currentline]

names.sort()

total = 0
for i in range(len(names)):
    sum = 0
    for char in names[i]:
        sum += ord(char) - 64
    total += sum * (i + 1)

print(total)