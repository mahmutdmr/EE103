from secret_data import secret_number

if secret_number < 0:
    print("Square root of negative numbers is not a real number.")
elif secret_number == 0:
    print("Approximate square root:", 0.0)
    print("Number of guesses:", 0)
else:
    epsilon = 0.01
    guess = secret_number / 2
    num_guesses = 0

    while abs(guess * guess - secret_number) >= epsilon:
        guess = guess - (guess * guess - secret_number) / (2 * guess)
        num_guesses += 1

    print("Approximate square root:", guess)
    print("Number of guesses:", num_guesses)
    print("Squared error:", abs(guess * guess - secret_number))
