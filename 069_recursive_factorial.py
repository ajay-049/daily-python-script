A=int(input("Enter a number that you want to find the factorial of: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(A))
