# This file is to compute the circumference and area of a circle
import math
try:
    r = float(input("Nhập vào bán kính của hình tròn: "))
    # Circumference
    c = 2*r*math.pi
    # Area
    a = r**2*math.pi
    print("Circumference of the circle is ",c)
    print("Area of the circle is ", a)
except:
    print("Error happens")
print("Thank you for using the app")
