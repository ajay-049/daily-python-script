A=int(input("Enter the first number: "))
B=int(input("Enter the second number: "))
C=int(input("Enter the third number: "))
if A>B and A>C:
    print("The largest number is:", A)
elif B>A and B>C:
    print("The largest number is:", B)
else:
    print("The largest number is:", C)