#Solved 
for x in range(0,1000000000000,2520):
    if x % 20 == 0 and x > 0:
        if x % 19 == 0:
            if x % 18 == 0:
                if x % 17 == 0:
                    if x % 16 == 0:
                        if x % 15 == 0:
                            if x % 14 == 0:
                                if x % 13 == 0:
                                    if x % 12 == 0:
                                        if x % 11 == 0:
                                            print(x)
                                            exit()
