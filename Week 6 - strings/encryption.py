import math

string = input("Please input a string: ")
new_str = ""

for c in string:
    if c.isdigit():
        new_c = ord(c) + 3
        if new_c > ord ("9"):
            new_c = new_c - ord("9") + ord ("1") - 1
    elif c.isalpha():
        new_c = ord(c) + 5
        if c.isupper() and new_c > ord("Z"):
            new_c = new_c - ord("Z") + ord("A") - 1
        elif c.islower() and new_c > ord("z"):
            new_c = new_c - ord("z") + ord("a") - 1
    else:
        new_c = ord(c)

    new_str = new_str + chr(new_c)

print ("The encrypted string is: ", new_str)