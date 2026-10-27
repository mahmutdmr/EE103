x = float(input("What x to find the square root of? "))
guess = float(input("What guess to start with? "))

if x < 0:
    print("Square root of negative numbers is not a real number.")
elif guess == 0:
    print("The starting guess cannot be zero.")
else:
    print("Current estimate squared:", guess ** 2)
    next_guess = guess - (guess ** 2 - x) / (2 * guess)
    print("Next guess:", next_guess)
