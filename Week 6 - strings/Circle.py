import math
radius = float(input("Please input radius of the circle: "))
pi = math.pi

circumference = 2*pi*radius
area = pi*radius**2

print("{:>4} Radius of Circle = {:>4.2f}, circumference = {:>4.2f}, area = {:>4.2f}".format("",radius,circumference,area))
