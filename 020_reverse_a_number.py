A=int(input("Enter a number: "))
reverse=0
while A>0:
    digit=A%10
    reverse=reverse*10+digit
    A//=10
print("The reverse of the number is:", reverse)