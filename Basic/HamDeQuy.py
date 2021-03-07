def factorial(n):
     if n == 0:
         return 1
     return n*factorial(n-1)

def fibonaci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

print(factorial(2))
print(factorial(4))
print(factorial(6))
print(fibonaci(4))
print(fibonaci(6))
