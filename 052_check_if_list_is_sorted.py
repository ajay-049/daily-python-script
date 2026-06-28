A =input("Enter a list of elements separated by spaces: ").split()
is_sorted = all(A[i] <= A[i+1] for i in range(len(A)-1))
if is_sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")