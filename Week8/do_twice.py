from math import sqrt


def f_x_twice(x, f_x):
    return f_x(f_x(x))


if __name__ == "__main__":
    print(f_x_twice(16, sqrt))
    print(f_x_twice(2, lambda x: x ** 2))
