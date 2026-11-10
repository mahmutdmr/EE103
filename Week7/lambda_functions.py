from functions_as_objects import calculator


is_even = lambda number: number % 2 == 0
square = lambda number: number ** 2
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b


if __name__ == "__main__":
    print(is_even(4))
    print(is_even(5))
    print(square(5))
    print(calculator(add, 3, 5))
    print(calculator(subtract, 3, 5))
    print(calculator(multiply, 3, 5))
    print(calculator(divide, 3, 5))
    print(calculator(lambda a, b: a + b, 3, 5))
    print(calculator(lambda a, b: a - b, 3, 5))
    print(calculator(lambda a, b: a * b, 3, 5))
    print(calculator(lambda a, b: a / b, 3, 5))
