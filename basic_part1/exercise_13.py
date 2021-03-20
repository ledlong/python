#  Write a Python program to compute the greatest common divisor (GCD) of two positive integers
a,b = eval(input("Input two integer numbers: "))
if a >= b:
    maxNum = a
    minNum = b
else:
    maxNum = b
    minNum = a

if minNum == 0:
    print("The greatest common divisor of {0} and {1} is {2}".format(maxNum, minNum, maxNum))
else:
    while True:
        quo = maxNum // minNum
        rem = maxNum % minNum
        if rem == 0:
            print("The greatest common divisor of {0} and {1} is {2}".format(a, b, minNum))
            break
        else:
            maxNum = minNum
            minNum = rem

# By deploying the idea of this program, the least common multiple can be easily found as:
# LCM(a,b) = |axb|/GCD(a,b)