A=input("Enter the first list (comma-separated): ").split(",")
B=input("Enter the second list (comma-separated): ").split(",")
result_dict = dict(zip(A, B))
print(result_dict)