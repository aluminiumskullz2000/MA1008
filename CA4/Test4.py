def evaluate(number1, op, number2):
    error = False
    try:
        num1 = float(number1)

        if (op  not in "+-*/%"):
            error = True
        
        num2 = float(number2)
    except ValueError:
        error = True

    if not error:
        if op == "+":
            value = num1 + num2
        elif op == "-":
            value = num1 - num2
        elif op == "*":
            value = num1 * num2
        elif op == "/":
            if num2 != 0: 
                value = num1 / num2
            else:
                error = True
                value = -999999
        elif op == "%":
            if num2 != 0: 
                value = num1 % num2
            else:
                error = True
                value = -99999
        else:
            value = -99999
    return value, error

while True:
    k = input("Enter input filename: ")
    try:
        infile = open(k,"r")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")
        
while True:
    j = input("Enter output filename: ")
    try:
        outfile = open(j, "w")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")

for L in infile:
    line = L.split()

    value, error = evaluate(line[0],  line[1], line[2])
    if not error:
        print(L.strip("\n"), "=" , value, file = outfile)
    else:
        print(L.strip("\n"), "is not a valid arithmetic operation", file = outfile)

infile.close()
outfile.close()
