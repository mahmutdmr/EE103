
x = 0.0
for iteration in range(10):
    x = x + 0.1

print("Result after adding 0.1 ten times:", x)
print("Expected result:", 1.0)
print("Is x exactly equal to 1.0?", x == 1.0)
print("Difference from 1.0:", abs(x - 1.0))
