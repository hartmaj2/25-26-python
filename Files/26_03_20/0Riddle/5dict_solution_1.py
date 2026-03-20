# Jaké má číslo uživatel, kterého zadáme?

# data
names = ["Jarda","Franta","Karel"]
phones = [774663989,608500600,777343232]

# code
name = input("Enter a name: ")
i = names.index(name)
number = phones[i]
print(f"{name} has phone number {number}")