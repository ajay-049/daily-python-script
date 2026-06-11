A=int(input("Enter a number: "))
B=A
reverse=0
while A>0:
    digit=A%10
    reverse=reverse*10+digit
    A//=10
if B==reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")