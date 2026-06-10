# Convert to int since prime numbers are integers
A = int(input("Enter a number: "))

# Numbers less than or equal to 1 are not prime
if A <= 1:
    print("The number is not prime.")
else:
    # Check if any number from 2 up to A-1 divides A perfectly
    is_prime = True
    for i in range(2, A):
        if A % i == 0:
            is_prime = False
            break  # Stop checking if we find a divisor

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
