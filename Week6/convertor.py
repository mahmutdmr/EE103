def binary_convertor(number):
    number = int(number)
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    number = abs(number)
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return sign + binary
