from secret_data import secret_number

if secret_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    epsilon = 0.01
    increment = 0.00001
    guess = 0.0
    num_guesses = 0

    while abs(guess * guess - secret_number) >= epsilon and guess * guess <= secret_number:
        guess += increment
        num_guesses += 1

    print("Approximate square root:", guess)
    print("Number of guesses:", num_guesses)
    print("Squared error:", abs(guess * guess - secret_number))
