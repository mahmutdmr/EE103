
x = 0

for i in range(10):
    x = x + 0.1

print(x)
print(f"{x:.1f}")
print(abs(x - 1) < 1e-12)
