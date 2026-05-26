a=int(input("Enter a number: "))
import random
random_number=random.randint(1,100)
print("The random number generated is:", random_number)
if a==random_number:
    print("Congratulations! You guessed the number correctly.")
elif a<random_number:
    print("Your guess is too low. Try again!")
else:    print("Your guess is too high. Try again!")