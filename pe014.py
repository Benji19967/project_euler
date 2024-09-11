#Solved (Took about 90seconds though)
def is_odd (n):
    if n % 2 != 0:
        return True
    else:
        return False



x = 1
dic = {1:1, 2:2, 3:8,}

for num in range(1,1000000):

    print("NEW NUMBER", num)

    y = num
    count = 0
    print(num)
    while num >= 1:
        if num == 1:
            count += 1
            break
        if is_odd(num):
            num = 3 * num + 1
        else:
            num = num / 2
        count += 1
        print(num, count)

        if num in dic:
            print("NUM", num)
            print("DIC", dic[num])
            count += dic[num]
            if count > x:
                x = count
                z = y
            break
    print("Count", count)
    dic.update({y:count})


    if count > x:
        x = count
        z = y

print("Longest chain:", x)
print("Number with Longest chain:", z)
