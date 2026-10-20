
target = 0.1
tolerance = 0.00001

remaining = target
approximation = 0.0
binary_digits = ""

max_bits = 64

while abs(approximation - target) >= tolerance and len(binary_digits) < max_bits:

    remaining *= 2

    bit = int(remaining)
    binary_digits += str(bit)
    remaining -= bit

    position = len(binary_digits)
    approximation += bit * (2 ** (-position))

print("Binary:", "0." + binary_digits)
print("Decimal approximation:", approximation)
print("Absolute error:", abs(approximation - target))
print("Tolerance achieved:", abs(approximation - target) < tolerance)
