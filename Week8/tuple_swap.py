x = 1
y = 2
x = y
y = x
print("Without temporary variable:", x, y)

x = 1
y = 2
temp = x
x = y
y = temp
print("With temporary variable:", x, y)

x = 1
y = 2
(x, y) = (y, x)
print("With tuple assignment:", x, y)
