while True:
    try:
        x = open("Text1.txt")
        y= open("Text2.txt","w")
        break
    except FileNotFoundError:
        print("Please edit the name of file.")
    
for i in range(1,4):
    A = x.readline()
    print(i, A, end="", file = y)
    
x.close()
y.close()
