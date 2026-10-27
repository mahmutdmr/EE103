this_year = 2026
year_as_string = str(this_year)
first_two = float(year_as_string[:2])
last_two = float(year_as_string[2:])
mysum = first_two + last_two
print(f"{mysum:.2f}")
if mysum == 46:
    print("Correct")
else:
    print("Wrong")
