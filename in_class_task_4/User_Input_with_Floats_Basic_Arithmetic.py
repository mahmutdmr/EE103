this_year = 2026
this_year = str(this_year)

first_two = this_year[:2]
last_two = this_year[2:]

first_two = float(first_two)
last_two = float(last_two)

mysum = first_two + last_two
print(f"{mysum:.2f}")
if mysum == 46:
    print("Correct")
else:
    print("Wrong")