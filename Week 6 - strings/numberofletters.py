input_string = input('Enter a sentence: ')

digits, upper, lower, others = 0, 0, 0, 0

for c in input_string:
    if c.isdigit():
        digits += 1
    elif c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    else:
        others += 1

print("Digits  Upper  Lower  Others")
print("{:^6d} {:^6d} {:^6d} {:^6d}".format(digits, upper, lower, others))
