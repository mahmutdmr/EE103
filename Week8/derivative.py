def estimate_derivative(func, x, h=1e-5):
    if h == 0:
        raise ValueError("h cannot be zero")
    return (func(x + h) - func(x - h)) / (2 * h)


def take_square(x):
    return x ** 2


if __name__ == "__main__":
    x = 3
    square_lambda = lambda value: value ** 2
    print("Derivative using take_square:", estimate_derivative(take_square, x))
    print("Derivative using lambda:", estimate_derivative(square_lambda, x))
    print("Expected result:", 2 * x)
