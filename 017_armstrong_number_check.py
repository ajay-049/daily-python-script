A=int(input("Enter a number: "))
sum=0
temp=A
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if A==sum:
    print(A,"is an Armstrong number")
else:
    print(A,"is not an Armstrong number")