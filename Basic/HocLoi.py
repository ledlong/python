try:
    a = float(input("Nhập vào 1 số:"))
    b = float(input("Nhập vào 1 số: "))
    c = a/b
    print("Result of {0}/{1} is {2}".format(a,b,c))
except:
    print("Error while performing the computation")