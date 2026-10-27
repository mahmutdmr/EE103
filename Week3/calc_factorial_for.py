number = int(input("Enter a nonnegative integer: "))
if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"{number}! = {factorial}")
