"""EE103 Week 5 Recap: solve the cupcake puzzle with nested guess-and-check loops."""

TOTAL_CUPCAKES = 28
found = False

# Guess every possible nonnegative number of cupcakes for all three people.
for david in range(TOTAL_CUPCAKES + 1):
    for emma in range(TOTAL_CUPCAKES + 1):
        for frank in range(TOTAL_CUPCAKES + 1):
            if (emma == david + 3 and
                    frank == 3 * david and
                    david + emma + frank == TOTAL_CUPCAKES):
                print(f"David packed {david} cupcakes!")
                print(f"Emma packed {emma} cupcakes!")
                print(f"Frank packed {frank} cupcakes!")
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print("No solution found.")
