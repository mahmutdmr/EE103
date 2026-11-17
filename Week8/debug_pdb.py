from derivative import estimate_derivative, take_square
from riemann_integral import integrate
from do_twice import f_x_twice
from mean_args import mean
from math import sqrt

x = 4
h = 1e-5
derivative = estimate_derivative(take_square, x, h)
area = integrate(take_square)
twice = f_x_twice(16, sqrt)
args = (1, 2, '3', 4, 5)
average = mean(*args)
import pdb
pdb.set_trace()
print(derivative, area, twice, average)
