import math

while True:
    a = float(input("Please key in the first coefficient of the equation: "))
    b = float(input("Please key in the second coefficient of the equation: "))
    c = float(input("Please key in the third coefficient of the equation: "))

    if (b**2 - 4*a*c) < 0:
        print ("No real roots") 
    else:
        print("x is", (- b + math.sqrt(b**2 - 4 * a * c )) / (2 * a) , "and" , (- b - math.sqrt(b**2 - 4 * a * c ))/ (2 * a) )