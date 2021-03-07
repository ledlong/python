# This program is to show how to access a list
# First method
list = [1, 556, 8, -89, -54, 0, 55, 77, -56, 7, 32, 66, -5445, 2, 996, 21]
oddList = []
evenList = []
primeList = []
negList = []

for x in list:
    print(x)
    if x % 2 == 0:
        evenList.append(x)
    if x % 2 != 0:
        oddList.append(x)
    if x < 0:
        negList.append(x)
    dem = 0
    if x > 0:
        for i in range(1, x + 1, 1):
            if x % i == 0:
                dem += 1
        if dem > 2:
            continue
        else:
            primeList.append(x)

print("The list of even number: ", evenList)
print("The list of odd number: ", oddList)
print("The list of negative number: ", negList)
print("The list of prime number: ", primeList)

list2 = list
list2[0] = 10
print(list)
# Second method
for i in range(0,len(list),1):
    print(list[i])