total = 0
dummy_range = range(10)
dummy_list_1 = list(dummy_range)
dummy_list_2 = []
for number in dummy_range:
    dummy_list_2.append(number)
print("First list:", dummy_list_1)
print("Second list:", dummy_list_2)
print("Lists are equal:", dummy_list_1 == dummy_list_2)
for number in dummy_list_1:
    total += number
print("Sum:", total)
