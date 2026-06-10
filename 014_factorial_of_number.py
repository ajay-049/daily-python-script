A=int(input("Enter a number: "))
factorial = 1
if A < 0:
    print("Factorial is not defined for negative numbers.")
elif A == 0 or A == 1:
    print("The factorial of", A, "is 1.")
else:
    for i in range(2, A + 1):
        factorial *= i
    print("The factorial of", A, "is", factorial)       