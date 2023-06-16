import keyword
variable = str(input("Please input a variable: "))
x = variable[0]
special_characters =  "" "`~!@#$%^&*()-+?=,[]|<>/."


if (x.isalpha() or x == "_") and (variable not in special_characters) and variable not in keyword.kwlist:
    print ("Valid")
else:
    print ("Invalid")

#decimal, numbers