fraction = float(input("Enter a fraction between 0 and 1 (try 0.1): "))
epsilon = 0.00001

if not 0 <= fraction < 1:
    print("Please enter a fraction between 0 (inclusive) and 1 (exclusive).")
else:
    original = fraction
    binary_digits = ""
    result = 0.0
    position = 0
    max_digits = 64

    while abs(result - original) >= epsilon and position < max_digits:
        fraction *= 2
        digit = int(fraction)
        binary_digits += str(digit)
        fraction -= digit
        position += 1
        result += digit * 2 ** (-position)

    print("Binary approximation: 0." + (binary_digits or "0"))
    print("Reconstructed decimal:", result)
    print("Absolute error:", abs(result - original))
    print("Within tolerance:", abs(result - original) < epsilon)
