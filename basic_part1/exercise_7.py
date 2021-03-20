# Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input a filename: ")
lis = filename.split(".")
print("Extension of the file name is: {0}".format(lis[len(lis)-1]))