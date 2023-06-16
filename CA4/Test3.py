def weightclass(weight):
    overweight = 0
    goodweight = 0
    underweight = 0
    error = 0
    try:
        if weight >= 85:
            overweight += 1
        elif weight < 85 and weight >55:
            goodweight += 1
        elif weight <= 55:
            underweight += 1
    except ValueError or TypeError:
        error += 1
    return overweight, goodweight, underweight, error

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

length = {}

for L in infile:
    weights = L.split(",")
    for weight in weights:
        overweight, goodweight, underweight, error = weightclass(weight)

print("Overwight people:   ", overweight, file=outfile)
print("Good-weight people: ", goodweight, file=outfile)
print("Underweight people: ", underweight, file=outfile)
print("Number of errors:   ", error, file=outfile)

infile.close()
outfile.close()

