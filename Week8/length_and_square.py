def length_and_square(L):
    squares = []
    for number in L:
        squares.append(number ** 2)
    return len(L), squares


if __name__ == "__main__":
    print(length_and_square([1, 3, 5]))
