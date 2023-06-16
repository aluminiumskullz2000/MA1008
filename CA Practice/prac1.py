# Write a program that reads in a sentence, and then prints the same sentence but with all upper case letters printed in lower case, and lower case letters in upper case.
# All other characters remain unchanged.
# You are not allowed to use Python string methods upper( ), lower( ), isupper() or islower(). Here is an example dialogue (underlined text is user input):
# Enter a sentence: 26 February, 2020 is a Wednesday.
# The output: 26 fEBRUARY, 2020 IS A wEDNESDAY.

import math
string = input("Please input a string: ")
new_str = " "

for i in string: 
    if i.isalpha():
        if i.isupper():
            j = ord(i) - (ord("A")-ord("a"))
        elif i.islower():
            j = ord(i) + (ord("A") - ord("a"))
    else:
        j = ord(i)
    
    new_str = new_str + chr(j)

print("The output is: ", new_str)