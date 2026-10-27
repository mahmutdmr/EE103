"""EE103 Week 5 Recap: multiply all integers in an inclusive range."""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

if start > end:
    print("Error: the start number must be less than or equal to the end number.")
else:
    # An empty product starts at 1, not 0.
    result_for = 1
    for number in range(start, end + 1):
        result_for *= number

    result_while = 1
    number = start
    while number <= end:
        result_while *= number
        number += 1

    print("For loop result:", result_for)
    print("While loop result:", result_while)

    if result_for == result_while:
        print("results are same")
    else:
        print("results are different")
