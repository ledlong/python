# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import *

print("Input the radius of a circle r = ")
r = float(input())
area = pi * r ** 2
print("Area of the circle is {0}".format(area))