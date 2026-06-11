A=int(input("Enter a decimal number: "))
binary=""
while A>0:
    binary=str(A%2)+binary
    A//=2
print("Binary equivalent:", binary)