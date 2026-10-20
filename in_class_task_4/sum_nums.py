n = int(input("Entter a number:"))
total = 0 
for i in range(1, n+1):
    total = total + i
print(f"Running Sum: {total}")

sum_gauss = n * (n+1)/2
print(f"Gauss Sum: {sum_gauss}")
if total == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")