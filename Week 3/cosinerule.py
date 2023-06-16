import math
#import math as m, can shorten the math. to just m
a = float(input("input a: "))
b = float(input("input b: "))
c = float(input("input c: "))

angle = math.acos((b**2 + c**2 - a**2)/2*b*c)

print (math.degrees(angle))
