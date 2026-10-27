name = input("Enter your name: ").upper()
s = "Aho54yu" + name + "42z.89tur"
name_from_slice = s[7:-9]
print(f"My name is {name_from_slice}")
print(f"My name in reverse order is {name_from_slice[::-1]}")
