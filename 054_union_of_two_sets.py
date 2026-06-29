A=[int(x) for x in input("Enter elements of first set: ").split()]
B=[int(x) for x in input("Enter elements of second set: ").split()]
C=list(A) + list(B)
D=sorted(list(set(C)))
print("Union of the two sets is:", D)