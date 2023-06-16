import math

hours_worked = float (input ("Please input total number of hours worked: " ))

if hours_worked <= 160:
    gross_pay = hours_worked * 10
else:
    gross_pay = (hours_worked - 160) * 15 + 160 * 10

if gross_pay <=1000:
    tax = gross_pay * 0.1
elif gross_pay > 1000 and gross_pay <= 1500:
    tax = (gross_pay - 1000) * 0.2 + 1000 * 0.1
else: 
    tax = (gross_pay - 1500) * 0.3 + 1000 * 0.1 + 500 * 0.2

net_pay = gross_pay - tax

print ("Gross pay is ", gross_pay)
print ("Tax is ", tax)
print ("Net pay is ", net_pay)