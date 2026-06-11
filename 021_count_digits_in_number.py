A=float(input("Enter a number: "))
count=0
while A>0:
    A//=10
    count+=1
print("Number of digits:", count)