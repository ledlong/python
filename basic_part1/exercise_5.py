"""Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them."""
name = input("Input your first name and last name: ")
lis = name.split(" ")
print(lis)
for x in range(len(lis)-1,-1,-1):
    print(lis[x],end=" ")