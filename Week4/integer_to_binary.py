number = int(input("Enter an integer: "))
original_number = number
number = abs(number)
binary_digits = ""

if number == 0:
    binary_digits = "0"
else:
    while number > 0:
        remainder = number % 2
        binary_digits = str(remainder) + binary_digits
        number //= 2

if original_number < 0:
    binary_digits = "-" + binary_digits
print(f"Binary representation of {original_number} is {binary_digits}")
