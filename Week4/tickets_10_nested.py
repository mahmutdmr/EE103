total = 10
found = False
for alyssa in range(total + 1):
    for ben in range(total + 1):
        for cindy in range(total + 1):
            if ben == alyssa - 2 and cindy == 2 * alyssa and alyssa + ben + cindy == total:
                print("Alyssa:", alyssa)
                print("Ben:", ben)
                print("Cindy:", cindy)
                found = True
                break
        if found:
            break
    if found:
        break
