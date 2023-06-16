# Write a program to evaluate the sine function accurate to 7 decimal places using the power series
# Note that the angle x is in radians. Check your result against the sin( ) function provided in the
# math library of Python for a value of x between –π and +π. Here is an example dialogue (underlined
# text is user input):
# Enter the angle (in radians): 2
# Power series : sin(2.0000) = 0.90929743
# Python library: sin(2.0000) = 0.90929743
# Comparison: The two values are equal.
# Note that the last comparison statement is the outcome of comparing the two sine values, not a
# direct print statement.

import math

epsilon = 1e-8
x = float(input("Please input angle(in radians): "))
growing_term = x
deno = 1
sum1 = 0
multiplier = 1
y = ""

while abs(growing_term) > epsilon:
    sum1 += growing_term
    multiplier += 2
    growing_term = -x**2*growing_term/(multiplier*(multiplier-1))

sin = math.sin(x)

if abs(sin-sum1)< epsilon:
    y = 'equal'
else:
    y = "not equal"

print("Power series : sin({}) = {}".format(x, sum1))
print("Python library : sin({}) = {}".format(x,sin))
print("Comparison: The two values are {}.".format(y))