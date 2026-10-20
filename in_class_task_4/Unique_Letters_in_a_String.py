s = "banana"
string_accumulator = ""
for char in s:
    if char not in string_accumulator:
        string_accumulator += char
print(len(string_accumulator))