"""Write a Python program which accepts a sequence of comma-separated
numbers from user and generate a list and a tuple with those numbers."""
seq = input("Insert a sequence of numbers which are separated by comma: ")
num = seq.split(",")
lis = []
tup = ()
for i in num:
    lis.append(i)
    tup = tup + (i,)
# Tuple can be obtained by casting a list: tup = tuple(lis)
print("List: ",lis)
print("Tuple: ",tup)