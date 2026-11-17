from derivative import estimate_derivative, take_square
from riemann_integral import integrate
from do_twice import f_x_twice
from math import sqrt

x = 3
h = 1e-5
print("x:", x)
print("h:", h)
print("f(x+h):", take_square(x + h))
print("f(x-h):", take_square(x - h))
print("Estimated derivative:", estimate_derivative(take_square, x, h))
steps = 4
print("Integration steps:", steps)
for i in range(steps):
    midpoint = (i + 0.5) / steps
    print("Midpoint:", midpoint, "Contribution:", take_square(midpoint) / steps)
print("Integral:", integrate(take_square, steps))
print("Do twice:", f_x_twice(16, sqrt))
