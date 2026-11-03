year = int(input("What year is this? "))
digits = str(abs(year))
digit_sum = 0
for digit in digits:
    digit_sum += int(digit)

average = digit_sum / len(digits)
print("Sum of digits:", digit_sum)
print("Average of digits:", average)
