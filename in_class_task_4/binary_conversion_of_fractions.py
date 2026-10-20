
fraction = float(input("Enter a fraction between 0 and 1: "))

if fraction < 0 or fraction >= 1:
    print("Please enter a value between 0 and 1.")

else:
    remaining = fraction
    binary_digits = ""
    max_bits = 32

    while remaining > 0 and len(binary_digits) < max_bits:
        remaining = remaining * 2
        bit = int(remaining)
        binary_digits += str(bit)
        remaining = remaining - bit

    if binary_digits == "":
        binary_digits = "0"

    print("Binary:", "0." + binary_digits)

    if remaining > 0:
        print("Stopped at maximum precision.")
