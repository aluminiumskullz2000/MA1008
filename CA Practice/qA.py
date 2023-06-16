# You are creating a new account and need to provide a password. The password has the following
# requirements:
# a) The password must have at least 6 characters and at most 20 characters.
# b) It must contain at least one lowercase letter, one upper case letter, and one digit. It may
# contain any other printable characters but not space.
# Write a python program that prompts the user to input a password and prints if the password is
# valid or invalid. Here are some sample dialogues (underlined text is user input):
# Enter Your Password: YYxx$$
# Invalid Password
# Enter Your Password: 33&Ds
# Invalid Password
# Enter Your Password: YYx3 rEE
# Invalid Password
# Enter Your Password: $3r.X9=+Ybc12E99
# Valid Password
# Enter Your Password: uuOObE3rE-9899erEETSYy
# Invalid Password

pw = input("Please provide a password: ")
lowercase = 0
uppercase = 0
digit = 0
othercharacters = 0

for i in pw:
    if ord(i) == ord(" "):
        break
    
    if i.isdigit():
        digit += 1
        print("digit")

    elif i.isalpha():
        if i.isupper():
            uppercase += 1
            print ("upper")
        elif i.islower():
            lowercase += 1
            print ("lower")
    elif not (i.isalpha() or i.isdigit()):
        othercharacters += 1
        print ("othercharacters")

total_characters = lowercase + uppercase + digit + othercharacters

if ((total_characters) >= 6 and (total_characters) <= 20) and digit >= 1 and lowercase >=1 and uppercase >=1:
    print("Valid Password")
else:
    print("Invalid Password")

print(lowercase)
print(uppercase)
print(digit)
print(othercharacters)
print(total_characters)
