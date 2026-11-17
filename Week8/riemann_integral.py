def integrate(func, steps=1000):
    if not isinstance(steps, int) or steps <= 0:
        raise ValueError("steps must be a positive integer")
    total_area = 0.0
    dx = 1 / steps
    for i in range(steps):
        midpoint = (i + 0.5) * dx
        total_area += func(midpoint) * dx
    return total_area


if __name__ == "__main__":
    print("Integral of x^2 from 0 to 1:", integrate(lambda x: x ** 2))
    print("Integral of x from 0 to 1:", integrate(lambda x: x))
