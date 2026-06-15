A = input("Enter a string: ")
B = A.replace(" ", "").lower()
if B == B[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")