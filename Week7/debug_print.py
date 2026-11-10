def count_evens(input_n):
    count = 0
    for num in range(input_n):
        print(f"[DEBUG] Checking num = {num}, Current count = {count}")
        if num % 2 == 0:
            count += 1
            print(f"[DEBUG] -> {num} is EVEN! Updated count = {count}")
    return count


if __name__ == "__main__":
    print("Total evens:", count_evens(5))
