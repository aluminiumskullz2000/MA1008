def checktype(x):
    try:
        x = int(x)
        y = "integer"        
    except ValueError:
        try: 
            x = float(x)
            y = "float"
        except ValueError:
            y = "error"
    return y
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
floatnumber = 0
integer = 0
error = 0
for L in infile:
    line = L.split(",")
    for i in line:
        y = checktype(i)
        if y == "float":
            floatnumber += 1
        elif y == "integer":
            integer += 1
        elif y == "error":
            error += 1

print("Number of floating point numbers:", floatnumber, file=outfile)
print("Number of integer numbers:", integer, file=outfile)
print("Number of errors:", error, file=outfile)

infile.close()
outfile.close()
