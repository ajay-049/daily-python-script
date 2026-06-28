A = [int(x) for x in input("Enter elements: ").split()]
A.sort(reverse=True)
print("The second largest element is:", A[1])