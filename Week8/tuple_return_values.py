def name_splitter(full_name):
    parts = full_name.strip().split(maxsplit=1)
    if len(parts) != 2:
        raise ValueError("Enter a first name and surname")
    return parts[0], parts[1]


def char_counts(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char in 'aeiou':
            vowels += 1
        elif 'a' <= char <= 'z':
            consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    print(name_splitter("Mahmut Demir"))
    print(char_counts("programming"))
