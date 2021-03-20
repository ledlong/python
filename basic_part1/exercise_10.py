# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
n = int(input("Input a positive integer number: "))
result = eval("{0}+{0}{0}+{0}{0}{0}".format(n))
print(result)