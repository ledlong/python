# Khởi tạo một ma trân MxN phần tử ngẫu nhiên
from random import randrange
M = int(input("Nhập vào số hàng: "))
N = int(input("Nhập vào số cột: "))
# Khởi tạo ma trận
matrix = []
for row in range(M):
    onerow = []
    for col in range(N):
        onerow.append(randrange(-100,100))
    matrix.append(onerow)
print(matrix)
for row in matrix:
    for elem in row:
        print("{0:>4}".format(elem),end='')
    print()
# Xuất ra một hàng nào đó
rowXuat = int(input("Nhập vào hàng bạn muốn xuất ra "))
print(matrix[rowXuat])
# Xuất ra một cột nào đó
colXuat = int(input("Nhập vào cột bạn muốn xuất ra "))
for row in range(M):
    for col in range(N):
        if col == colXuat:
            print("{0:>4}".format(matrix[row][col]))
# Xuất ra giá trị cực đại của ma trận
maxValue = matrix[0][0]
for row in matrix:
    for elem in row:
        if elem > maxValue:
            maxValue = elem
print("Giá trị cực đại là: ", maxValue)