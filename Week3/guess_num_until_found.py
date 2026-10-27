# Part 3: keep asking until the number is found.
from secret_number import secretNum

while True:
    guess = int(input("Guess the secret number: "))
    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        print("You found the secret number!")
        break
