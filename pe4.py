#Solved 

def pal(n):
    if n >= 100000:
        a = n % 10
        b = int((n % 100) / 10)
        c = int((n % 1000) / 100)
        d = int((n % 10000) / 1000)
        e = int((n % 100000) / 10000)
        f = int((n % 1000000) / 100000)
        if a == f and b == e and c == d:
            return True
        return False
    else:
        a = n % 10
        b = int((n % 100) / 10)
        c = int((n % 1000) / 100)
        d = int((n % 10000) / 1000)
        e = int((n % 100000) / 10000)
        if a == e and b == d:
            return True
        return False

ans = 10001
for x in range(100,1000):
    for y in range(100,1000):
        z = x * y
        if pal(z) and z > ans:
            ans = z
print(ans)
