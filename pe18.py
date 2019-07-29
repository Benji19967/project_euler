# How to read from a file

f = open('pe18.txt', 'r')

lines = f.read().split('\n')

w, h = 15, 15
count = 0

matrix = [[0 for x in range (w)] for y in range(h)] # w = number of columns, h = number of rows

for x in range(0, 15):
    matrix[x] = lines[x].split(' ')

def max_path(x, y):
    current = int(matrix[x][y])
    
    if(x == 14):
         return current

    left = max_path(x+1, y)
    right = max_path(x+1, y+1)
    return current + max(left, right)


print(max_path(0, 0))
