
number = float(input("Enter a number (e.g. 13.375): "))

if not (-float("inf") < number < float("inf")):
    print("Please enter a finite number.")
else:
    sign = "-" if number < 0 else ""
    value = abs(number)
    integer_part = int(value)
    fraction_part = value - integer_part

    # Integer part: divide by 2 and collect remainders.
    integer_copy = integer_part
    integer_binary = "0" if integer_copy == 0 else ""
    while integer_copy > 0:
        integer_binary = str(integer_copy % 2) + integer_binary
        integer_copy //= 2

    # Fractional part: multiply by 2 and collect integer digits.
    fractional_binary = ""
    max_fraction_digits = 32  # Limit repeating binary fractions.
    digits = 0
    while fraction_part > 0 and digits < max_fraction_digits:
        fraction_part *= 2
        digit = int(fraction_part)
        fractional_binary += str(digit)
        fraction_part -= digit
        digits += 1

    if fractional_binary:
        binary = f"{sign}{integer_binary}.{fractional_binary}"
    else:
        binary = f"{sign}{integer_binary}"

    print(f"Binary representation of {number} is {binary}")
    if fraction_part > 0:
        print(f"Note: showing the first {max_fraction_digits} fractional binary digits (truncated).")
