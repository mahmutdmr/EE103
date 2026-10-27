"""EE103 Week 5 Tasks, Part 2: find a favorite page by bisection search."""

low = 1
high = 148
num_guesses = 0

print("Think of a secret page from 1 to 148.")
print("For every guess, type 'higher', 'lower', or 'correct'.")

while low <= high:
    guess = (low + high) // 2
    num_guesses += 1
    answer = input(f"Is your page {guess}? [higher/lower/correct]: ").strip().lower()

    if answer in ("correct", "c"):
        print(f"Found your favorite page: {guess}")
        print(f"Number of guesses: {num_guesses}")
        break
    elif answer in ("higher", "h"):
        low = guess + 1
    elif answer in ("lower", "l"):
        high = guess - 1
    else:
        print("Please enter 'higher', 'lower', or 'correct'.")
        num_guesses -= 1  # An invalid response is not a completed guess.
else:
    print("There is no page matching these hints. Please check your answers.")
