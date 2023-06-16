import math

def area(number1, number2, shape = "cir"):
    if shape == "cir":
        area = math.pi * number1 ** 2
        return area
    elif shape == "rect":
        area = number1 * number2
        return area
    elif shape == "tri":
        area = 0.5 * number1 * number2
        return area
