N = int(input("Nhập chiều cao của chữ cái N = "))
# Letter N
for ii in range (0,N,1):
    for jj in range (0,N,1):
        if jj == 0 or ii == jj or jj == N-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()

# Letter P
for ii in range (0,N,1):
    for jj in range (0,N,1):
        if jj == 0 or (jj == (N-1) and ii <= N/2) or ii == 0 or ii == N/2:
            print("*",end="")
        else:
            print("",end="")
    print()