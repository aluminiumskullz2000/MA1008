import math

input("please input the values")

a1 = int(input("a1: "))
b1 = int(input("b1: "))
c1 = int(input("c1: "))
a2 = int(input("a2: "))
b2 = int(input("b2: "))
c2 = int(input("c2: "))

x = (b2*c1-b1*c2)/(a1*b2-a2*b1)
print ("x = " , x )

y = (a1*c2-a2*c1)/(a1*b2-a2*b1)
print ("y = " , y )
