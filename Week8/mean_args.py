def mean(*args):
    if not args:
        raise ValueError("At least one number is required")
    tot = 0.0
    for arg in args:
        tot += float(arg)
    return tot / len(args)


if __name__ == "__main__":
    print(mean(4, 6, 8))
    print(mean(1, 2, 3, 4, 5))
    print(mean(1, 2, '3', 4, 5))
    dummy1 = (3)
    dummy2 = (3,)
    print(type(dummy1))
    print(type(dummy2))
