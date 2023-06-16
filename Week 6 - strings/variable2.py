var = input("Enter a variable: ")
valid = "Invalid"

if var[0].isalpha() or var[0] == "_":  # check first character
    valid = "Valid"
    for c in var:  # check the rest one by one
        if not (c.isdigit() or c.isalpha() or c == '_'):
           valid = "Invalid"
           break

print("Valid variable? ", valid)
