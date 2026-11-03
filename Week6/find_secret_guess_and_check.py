from secret_data import secret_year

num_guesses = 0
for guess in range(2027):
    num_guesses += 1
    if guess == secret_year:
        print("Secret year:", guess)
        print("Number of guesses:", num_guesses)
        break
else:
    print("The secret year is outside the range 0 to 2026.")
