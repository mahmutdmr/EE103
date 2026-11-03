x = 0.1
y = 0.2
result = x + y

print("Result:", result)
print("Exactly equal to 0.3:", result == 0.3)
print("Close enough to 0.3:", 0.3 - 1e-4 <= result <= 0.3 + 1e-4)
