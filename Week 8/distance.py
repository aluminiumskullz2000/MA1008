import math

g = 9.81

def hori_dist(velocity,angle_in_radians,initial_height):
    horizontal = (velocity**2/(2*g))*(1+(math.sqrt(1+(2*g*initial_height)/(velocity**2*(math.sin(angle_in_radians))**2))))*math.sin(2*angle_in_radians)