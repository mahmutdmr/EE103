"""EE103 Week 5 Tasks, Part 1: square root by incremental approximation.

The assignment checks abs(guess**2 - number) < epsilon (squared residual),
not abs(guess - math.sqrt(number)) < epsilon (root error).
"""

import math

number = float(input("Enter a number to find its square root: "))

if not math.isfinite(number):
    print("Error: the input must be a finite number.")
elif number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    epsilon = 0.01
    increment = 0.0001  # Try changing to 0.00001 for more precise results.
    num_guesses = 0
    guess = 0.0
    DEBUG = False  # Change to True to print the guess every 1000 iterations.

    # Stop either after reaching the accepted error OR upon overshooting.
    while abs(guess**2 - number) >= epsilon and guess**2 <= number:
        previous_guess = guess
        guess += increment
        num_guesses += 1

        if DEBUG and num_guesses % 1000 == 0:
            print("Current guess =", guess)

        # Extra defense for extremely large inputs / tiny increments.
        if guess == previous_guess:
            print("Warning: floating-point precision prevents further progress.")
            break

    error = abs(guess**2 - number)
    print("Number of guesses:", num_guesses)
    print("Approximated square root:", guess)
    print("Absolute squared error:", error)

    if error < epsilon:
        print("Success: approximation is within epsilon.")
    else:
        print("Tolerance not reached (overshoot or insufficient precision).")
        print("Try reducing increment from 0.0001 to 0.00001 and run again.")
