from time import perf_counter

total = 1000

# Method 1: Nested loops
start = perf_counter()
nested_answer = None
nested_checks = 0

for alyssa in range(total + 1):
    cindy = 2 * alyssa
    for ben in range(total + 1):
        nested_checks += 1
        if alyssa - ben == 20 and alyssa + ben + cindy == total:
            nested_answer = (alyssa, ben, cindy)

nested_time = perf_counter() - start

# Method 2: Single loop
start = perf_counter()
single_answer = None
single_checks = 0

for alyssa in range(total + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    single_checks += 1

    if ben >= 0 and alyssa + ben + cindy == total:
        single_answer = (alyssa, ben, cindy)

single_time = perf_counter() - start

print("Nested answer:", nested_answer)
print("Single answer:", single_answer)
print("Nested checks:", nested_checks)
print("Single checks:", single_checks)
print(f"Nested time: {nested_time:.6f} s")
print(f"Single time: {single_time:.6f} s")
