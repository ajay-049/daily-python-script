A=input("Enter a binary number: ")
decimal=0
power=0
for i in reversed(A):
    if i=='1':
        decimal+=2**power
    power+=1
print("Decimal equivalent:", decimal)