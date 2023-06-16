import math

x = int (input ("Please enter start value: "))
y = int (input ("Please enter end value: "))
z = int (input ("Please enter increment: "))

while x < y+1:
    sgd = round(x / 3.03,2)
    print ("rm", x , " = SGD$", sgd)
    x += 1