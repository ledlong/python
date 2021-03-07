from math import sin

x1,x2 = eval(input("Nhập vào giá trị x1, x2: "))
x3 = eval("x1+x2-x2*sin(x1)")
if x1 > x2:
    maxVal = x1
else:
    maxVal = x2
print("Giá trị cực đại là:", maxVal)
print(x3)