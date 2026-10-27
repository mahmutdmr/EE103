number = int(input("Enter a nonnegative integer: "))
if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"{number}! = {factorial}")
