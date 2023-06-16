import math

weight = float(input ("Weight in kg = "))
height = float(input ("Height in m = "))

BMI = (weight / height**2)
BMI = str(round(BMI,2))

print ("Your BMI is ", BMI)
