def sqrt_guess_and_check(number):
    if number < 0:
        raise ValueError("Cannot calculate the real square root of a negative number")
    guess = 0
    while guess * guess < number:
        guess += 1
    if guess > 0 and abs((guess - 1) ** 2 - number) < abs(guess ** 2 - number):
        return guess - 1
    return guess


def sqrt_approximation(number, epsilon=0.01, increment=0.0001):
    if number < 0:
        raise ValueError("Cannot calculate the real square root of a negative number")
    if increment <= 0 or epsilon <= 0:
        raise ValueError("Epsilon and increment must be positive")
    guess = 0.0
    while abs(guess ** 2 - number) >= epsilon:
        next_guess = guess + increment
        if next_guess == guess:
            break
        if next_guess ** 2 > number and guess ** 2 < number:
            increment /= 10
        else:
            guess = next_guess
    return guess


def sqrt_bisection_search(number, epsilon=0.01):
    if number < 0:
        raise ValueError("Cannot calculate the real square root of a negative number")
    if epsilon <= 0:
        raise ValueError("Epsilon must be positive")
    low = 0.0
    high = max(1.0, float(number))
    guess = (low + high) / 2
    while abs(guess ** 2 - number) >= epsilon:
        if guess ** 2 < number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess


if __name__ == "__main__":
    print("Guess and Check: test consecutive integer guesses and choose the closest square.")
    print("Approximation: increase a fractional guess until the squared error is small.")
    print("Bisection Search: repeatedly halve an interval that contains the square root.")
    number = float(input("Enter a number to find its square root: "))
    if number < 0:
        print("Square root of negative numbers is not a real number.")
    else:
        print("Guess and Check:", sqrt_guess_and_check(number))
        print("Approximation:", sqrt_approximation(number))
        print("Bisection Search:", sqrt_bisection_search(number))
