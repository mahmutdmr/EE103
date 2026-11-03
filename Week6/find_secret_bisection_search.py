from secret_data import secret_year

low = 0
high = 2026
num_guesses = 0

while low <= high:
    guess = (low + high) // 2
    num_guesses += 1
    if guess == secret_year:
        print("Secret year:", guess)
        print("Number of guesses:", num_guesses)
        break
    elif guess < secret_year:
        low = guess + 1
    else:
        high = guess - 1
else:
    print("The secret year is outside the range 0 to 2026.")
