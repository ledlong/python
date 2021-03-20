# Write a Python program to get the current username
from getpass import getpass
import socket as s

print(getpass.getuser())
print(s.gethostname())

passwd = getpass("password: ")
print(passwd)