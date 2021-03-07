print("Professional Python in 4 weeks")
x = 1
y = 4
z = x+y
print("{0} + {1} = {2}".format(x,y,z))
# Check type of a variable
"""
This part is to explain that this part is for commenting
"""
import sys
print(sys.float_info)
print(sys.int_info)

del(x)
q = complex(2,3)
print(q)
q1 = q.real
q2 = q.imag
print("The complex number {0} has real part of {1} and imaginary part of {2}".format(q,q1,q2));

print('''Hello
everyone
I'm Long Le''')

print("Hello")

l = 5
if not l >= 10:
    print("True")
else:
    print("False")

x = 5
y = 5
if (x is y):
    print("They are equal")
else:
    print("They are not equal")


