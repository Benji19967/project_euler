#Solved

one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4

sum_9 = 3+3+5+4+4+3+5+5+4
print(sum_9) #36

ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
sum_19 = sum_9 + 3+6+6+8+8+7+7+9+8+8
print(sum_19) #107


twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
sum_99 = sum_19 + 8*sum_9 + 60+60+50+50+50+70+60+60
print(sum_99) #863

hundred = 7
_and_ = 3
onethousand = 11
sum_100_up = 900*7 + 100*sum_9 + 99*9*3 + 9*sum_99 + 11

total = sum_99 + sum_100_up
print(total)
