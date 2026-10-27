s = input("Enter lowercase letters: ")
unique_letters = ""
for letter in s:
    if letter not in unique_letters:
        unique_letters += letter
print("Number of unique letters:", len(unique_letters))
