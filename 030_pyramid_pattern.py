A = int(input("Enter the number of rows: "))
for i in range(A):
    for j in range(A-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()