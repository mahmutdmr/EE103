# Part 4: after five incorrect guesses, demonstrate an infinite loop.
# Stop the program with Ctrl+C if that happens.
from secret_number import secretNum

found = False
for attempt in range(1, 6):
    guess = int(input(f"Guess {attempt}/5: "))
    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        print("You found the secret number!")
        found = True
        break

if not found:
    while True:
        print("Oh! Noooooo…")
