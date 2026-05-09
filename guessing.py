import random

acno = random.randint(1, 10)

guess = 0

while guess != acno:

    guess = int(input("Guess the number (1-10): "))

    if guess > acno:
        print("Too high")

    elif guess < acno:
        print("Too low")

    else:
        print("Yayyy that's the right number!")

print("The number was:", acno)
