import math
n = 0
for x in range (1900,2100):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) :
        print (x, end=" ")
        n+=1
        if n%8 == 0:
            print()

