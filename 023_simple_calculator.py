A=float(input("Enter the first number: "))
B=float(input("Enter the second number: "))
operation=input("Enter the operation (+, -, *, /): ")

if operation=="+":
    print("Result:", A+B)
elif operation=="-":
    print("Result:", A-B)
elif operation=="*":
    print("Result:", A*B)
elif operation=="/":
    print("Result:", A/B)
else:
    print("Invalid operation.")