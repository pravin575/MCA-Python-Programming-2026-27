secret_number = 50

guess = int(input("Guess the number: "))

while guess != secret_number:

    if guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Guess again: "))

print("Congratulations! You guessed the correct number.")
