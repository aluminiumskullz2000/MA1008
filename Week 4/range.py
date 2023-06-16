import math
while True:
    a = int (input ("Please input the first integer: "))
    b = int (input ("Please input the second integer: "))
    c = int (input ("Please input the third integer: "))
    list = {a, b, c}

    maximum = max(list)
    minimum = min(list)
        
    print ("The range is between ", minimum ," and ", maximum)