stringVal = "Le Duong Long"
# Traditional way to use for loop
for i in stringVal:
    print(i)
# To use iterator to print an array
iteration = iter(stringVal)
n = 1
while n <= len(stringVal):
    print(iteration.__next__(),end="")
    n += 1