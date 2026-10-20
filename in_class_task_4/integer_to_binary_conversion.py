
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")

elif number == 0:
    print("Binary: 0")

else:
    n = number
    remainders = ""

    while n > 0:
        remainder = n % 2
        remainders += str(remainder)
        n = n // 2

    binary = remainders[::-1]
    print("Binary:", binary)
