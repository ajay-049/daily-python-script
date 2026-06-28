A=input("Enter a list of elements separated by spaces: ").split()
n = int(input("Enter the number of positions to rotate the list: "))
n = n % len(A)  # Handle cases where n is greater than the length of the list
rotated_list = A[-n:] + A[:-n]
print("The rotated list is:", rotated_list)