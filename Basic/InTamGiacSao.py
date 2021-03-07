# Chương trình này in ra tam giác sao
n = 0
while n <= 0:
    n = int(input("Nhập vào một số n = "))

# Chương trình này in ra tam giác vuông trái
for ii in range (1,n + 1,1):
    print("* "*ii)

# Chương trình này in ra tam giác đều
for ii in range (1,n + 1,1):
    print(" "*(n-ii),"* "*ii)

# Chương trình này in ra tam giác vuông phải
for ii in range (1,n + 1,1):
    print("  "*(n-ii),"* "*ii)

# Chương trình này in ra tam giác đều lộn ngược
for ii in range (n, 0, -1):
    print(" "*(n-ii),"* "*ii)