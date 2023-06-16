import math

year = int ( input ("Please input the year: "))
# can use and not as well
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print ("Leap Year")
else: 
    print ("Not a leap year")
