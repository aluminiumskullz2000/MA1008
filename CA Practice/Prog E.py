# MA1008 CA 2 
# evaluate the power series for sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

import math

x = float(input("Enter the angle (in radians): "))

sum = 0.0     # for sum of the series
eps = 1e-10   # epsilon, very small number for checking convergence
term = x      # value of individual terms, start with first term = x
n = 1         # n is the power of x, also for factorial in denominator

# note that individual terms will get smaller and smaller and eventually go below eps

while abs(term) > eps:   # loop through the terms, check each against eps
   sum = sum + term      # add each term to the sum
   n = n + 2             # power & factorial jump by 2 for the next term 
   term = -x*x*term/(n*(n-1))  # evaluate next term, note the repeat pattern
                               # in the terms including the - sign that
                               # flips the terms between +ve and -ve

# exit point from above loop, the series has terminated due to term <= eps

py_sin = math.sin(x)   # this is sine value from Python library
print("\nPower series  : sin({:.4f}) = {:.8f}". format(x, sum))
print("Python library: sin({:.4f}) = {:.8f}". format(x, py_sin))

# make comparison
print("Comparison:", end = " ")
if abs(py_sin - sum) < eps:   # check if the two values are very nearly equal
   print("The two values are equal.")
else:
   print("The two values are not equal.")
