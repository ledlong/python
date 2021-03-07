def handle(f,x):
    return f(x)

def handleTwoVars(f,x,y):
    return f(x,y)

def evenOdd(x):
    if x % 2 == 0:
        print("x is an even number")
    else:
        print("x is an odd number")

def primeNumber(x):
    dem = 0
    for i in range(1,x+1,1):
        if x % i == 0:
            dem += 1
    if dem == 2:
        print("{0} is a prime number".format(x))
    else:
        print("{0} is not a prime number".format(x))

def addTwoVars(x,y):
    return x+y

result1 = handle(lambda x:evenOdd(x),6)
result2 = handle(lambda x:primeNumber(x),13)
result3 = handle(lambda x:primeNumber(x),10)
result4 = handleTwoVars(lambda x,y:addTwoVars(x,y),10,5)
print(result4)