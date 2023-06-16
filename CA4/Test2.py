def weightcategory(weight):
    overweight = 0
    good_weight = 0
    underweight = 0
    error = 0
    try:
        weight = float(weight)
        if weight >= 85:
            overweight += 1
        elif weight < 85 and weight > 55:
            good_weight += 1
        else:
            underweight += 1
    except ValueError:
        error += 1
    return overweight, good_weight, underweight, error

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
maxvowels = 0

for L in infile:
    weights = L.split(",")
    for weight in weights:
        overweight, good_weight, underweight, error = weightcategory(weight)

print

infile.close()
outfile.close()
    
