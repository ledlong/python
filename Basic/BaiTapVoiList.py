from random import randrange

N = int(input("Input the number of elements: "))
lis = []
# Initialize N random elements of a list
for i in range(N):
    lis.append(randrange(-100, 100))
print(lis)
# Insert a number amd delete that number from the list
newNum = int(input("Insert new number: "))
lis.append(newNum)
print(lis)
number = int(input("Please insert a number that you want to delete: "))
while lis.count(number) > 0:
    lis.remove(number)
print(lis)