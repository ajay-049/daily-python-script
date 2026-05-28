A=int(input("Enter a year: "))
if (A%4==0 and A%100!=0) or (A%400==0):
    print("The year is a leap year.")
else:    print("The year is not a leap year.")
