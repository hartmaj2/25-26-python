# Jaké má číslo uživatel, kterého zadáme?

# data
phones = { "Jarda" : 774663989, "Franta" : 608500600, "Karel" : 777343232 }

# code
name = input("Enter a name: ")
number = phones[name]
print(f"{name} has phone number {number}")