import math

x = int (input ("Please enter start value: "))
y = int (input ("Please enter end value: "))
z = int (input ("Please enter increment: "))

for a in range(x,y+1,z):
    rm = a *3.03
    print ("SGD$", a , " = RM", rm)
    