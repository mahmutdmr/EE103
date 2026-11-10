from is_even_or_odd import is_even_or_odd


def calculator(operation, x, y):
    return operation(x, y)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def count_even(check_function, n):
    count = 0
    for number in range(n):
        if check_function(number) == "even":
            count += 1
    return count


if __name__ == "__main__":
    is_even_or_odd_alias = is_even_or_odd
    print(is_even_or_odd(4), is_even_or_odd_alias(4))
    print(is_even_or_odd(5), is_even_or_odd_alias(5))
    print(is_even_or_odd(4.0), is_even_or_odd_alias(4.0))
    for operation in (add, subtract, multiply, divide):
        print(operation.__name__, calculator(operation, 3, 5), operation(3, 5))
    print("Count even in range(5):", count_even(is_even_or_odd, 5))
