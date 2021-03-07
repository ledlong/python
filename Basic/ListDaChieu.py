from random import randrange

matrix = [
    [100,14,8,22,71],
    [0,243,68,1,30],
    [90,21,7,67,112],
    [115,200,70,150,8]
]

print(matrix)

for row in matrix:
    for elem in row:
        print('{0:>4}'.format(elem),end='')
    print()

col = 3
row = 5
list = [[1]*col]*row
print(list)

for row in list:
    for elem in row:
        print('{0:>4}'.format(elem),end='')
    print()

arr2D = []
rowsize = 5
colsize = 3
for row in range(rowsize):
    onerow = []
    for col in range(colsize):
        onerow.append(randrange(-100,100))
    arr2D.append(onerow)
print(arr2D)

for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print("{0:>6}".format(arr2D[i][j]),end='')
    print()
