from derivative import estimate_derivative, take_square
from riemann_integral import integrate
from do_twice import f_x_twice
from math import sqrt


def run_calculations():
    x = 3
    h = 1e-5
    derivative = estimate_derivative(take_square, x, h)
    steps = 1000
    area = integrate(take_square, steps)
    twice = f_x_twice(16, sqrt)
    return derivative, area, twice


if __name__ == "__main__":
    print(run_calculations())
