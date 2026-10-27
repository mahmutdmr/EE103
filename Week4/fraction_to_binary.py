fraction = float(input("Enter a fraction between 0 and 1: "))
if not 0 <= fraction < 1:
    print("Please enter a fraction between 0 (inclusive) and 1 (exclusive).")
else:
    binary_digits = ""
    max_digits = 32
    count = 0
    while fraction > 0 and count < max_digits:
        fraction *= 2
        digit = int(fraction)
        binary_digits += str(digit)
        fraction -= digit
        count += 1
    print("Binary representation: 0." + (binary_digits or "0"))
    if fraction > 0:
        print("The expansion was truncated after 32 binary digits.")
