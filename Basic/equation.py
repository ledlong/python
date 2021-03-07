from HamBacNhat import hamBacNhat
from math import sqrt

# Input the order of equation
N = int(input("Input the order of equation "))
if N == 1:
    a, b = eval(input("Input the coefficients a and b: "))
    hamBacNhat(a,b)
elif N == 2:
    a, b, c = eval(input("Input the coefficients a, b, c: "))
    if a == 0:
        hamBacNhat(b,c)
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            print("This equation has one solution x = {0}".format(-b/(2*a)))
        elif delta < 0:
            print("This equation has no solution")
        else:
            print("This equation has two distinguish solutions x1 = {0} and x2 = {1}".format((-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a)))
else:
    pass


