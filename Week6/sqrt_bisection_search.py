from secret_data import secret_number

if secret_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    epsilon = 0.01
    low = 0.0
    high = max(1.0, float(secret_number))
    guess = (low + high) / 2
    num_guesses = 0

    while abs(guess * guess - secret_number) >= epsilon:
        num_guesses += 1
        if guess * guess < secret_number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2

    print("Approximate square root:", guess)
    print("Number of guesses:", num_guesses)
    print("Squared error:", abs(guess * guess - secret_number))
