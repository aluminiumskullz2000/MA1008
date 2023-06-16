x =open("ASCIITable.txt","w")
for i in range(0,128):
    string = "{:3d} {:3d}: {:3s}".format(i+1, i, chr(i))
    print(string, file = x)
    
x.close()
