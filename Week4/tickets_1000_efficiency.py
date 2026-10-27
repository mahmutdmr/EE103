from time import perf_counter

total = 1000

# Nested guess-and-check: test Alyssa, Ben and Cindy.
start_time = perf_counter()
checks_nested = 0
found_nested = False
for alyssa in range(total + 1):
    for ben in range(total + 1):
        if ben != alyssa - 20:
            continue
        for cindy in range(total + 1):
            checks_nested += 1
            if cindy == 2 * alyssa and alyssa + ben + cindy == total:
                print("Nested loop: Alyssa =", alyssa, "Ben =", ben, "Cindy =", cindy)
                found_nested = True
                break
        if found_nested:
            break
    if found_nested:
        break
nested_duration = perf_counter() - start_time

# One loop: determine Ben and Cindy directly for each Alyssa guess.
start_time = perf_counter()
checks_single = 0
for alyssa in range(total + 1):
    checks_single += 1
    ben = alyssa - 20
    cindy = 2 * alyssa
    if ben >= 0 and alyssa + ben + cindy == total:
        print("Single loop: Alyssa =", alyssa, "Ben =", ben, "Cindy =", cindy)
        break
single_duration = perf_counter() - start_time

print("Nested loop candidate checks:", checks_nested)
print("Single loop guesses:", checks_single)
print(f"Nested loop time: {nested_duration:.6f} seconds")
print(f"Single loop time: {single_duration:.6f} seconds")
