
number = 0.1
epsilon = 0.00001
fraction = number
result = 0.0
binary_digits = ""
num_digits = 0
max_digits = 64  # Safety guard against a non-terminating loop.

while abs(result - number) >= epsilon and num_digits < max_digits:
    fraction *= 2
    digit = int(fraction)
    binary_digits += str(digit)
    fraction -= digit

    num_digits += 1
    result += digit * (2 ** (-num_digits))

print("Decimal number:", number)
print("Approximate binary representation: 0." + binary_digits)
print("Reconstructed decimal value:", result)
print("Absolute error:", abs(result - number))
print("Number of fractional binary digits:", num_digits)
print("Within tolerance?", abs(result - number) < epsilon)
