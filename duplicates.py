s = input("Enter a string: ")
unique = ""

for ch in s:
    if ch not in unique:
        unique += ch

print("Unique string:", unique)
