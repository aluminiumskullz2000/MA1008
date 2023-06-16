while True:
    try:
        A = input ("Please input first file name:")
        B = input ("Please input second file name:")
        x = open(A)
        y= open(B,"w")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")
    
for line in x:
    line = line.upper()
    print(line, end="", file = y)

x.close()
y.close()
