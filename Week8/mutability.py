my_list = [1, 3, 5]
my_tuple = (1, 3, 5)
my_list[1] = 5
print("Changed list:", my_list)
try:
    my_tuple[1] = 5
except TypeError as error:
    print("Tuple change:", type(error).__name__)
print("Tuple:", my_tuple)
