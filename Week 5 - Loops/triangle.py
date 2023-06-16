import math

h = 3
pattern = ""

for i in range(1,h+1):
    if i % 2 == 1:
        pattern = "AA" + pattern
    else:
        pattern = "BB" + pattern

    print (pattern)

#i for the rows, j for the columns (nested for loops)
#make it symmetric