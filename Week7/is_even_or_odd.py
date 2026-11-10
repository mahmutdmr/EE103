def is_even_or_odd(number):
    if type(number) is not int:
        return "unknown"
    if number % 2 == 0:
        return "even"
    return "odd"


if __name__ == "__main__":
    print(is_even_or_odd(4))
    print(is_even_or_odd(5))
    print(is_even_or_odd(4.0))
