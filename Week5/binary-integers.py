"""EE103 Week 5 Recap: integer-to-binary conversion by repeated division by 2."""

number = int(input("Enter an integer: "))
original_number = number

# Apply the algorithm to the absolute value and restore the sign at the end.
number = abs(number)
if number == 0:
    binary_digits = "0"
else:
    binary_digits = ""
    while number > 0:
        remainder = number % 2
        binary_digits = str(remainder) + binary_digits
        number //= 2

if original_number < 0:
    binary_digits = "-" + binary_digits

print(f"Binary representation of {original_number} is {binary_digits}")
