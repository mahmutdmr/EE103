number = int(input("Enter a nonnegative integer: "))
if number < 0:
    print("Enter a nonnegative integer.")
else:
    running_sum = 0
    for i in range(1, number + 1):
        running_sum += i

    sum_gauss = number * (number + 1) // 2
    print("Running sum:", running_sum)
    print("Gauss sum:", sum_gauss)
    if running_sum == sum_gauss:
        print("My running sum code works correctly")
    else:
        print("My running sum code failed badly")
