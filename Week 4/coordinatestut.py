import math

while True:
    x = float(input("Please input the x-coordinate: "))
    y = float(input("Please input the y-coordinate: "))
    epsilon = 1e-7

    if abs(x) < epsilon:
        if abs(y) < epsilon:
            print("The point lies on the origin.")
        elif abs(y) > epsilon:
            print ("The point lies on the x - axis.")
    elif abs(y) < epsilon:
        if abs(x) > epsilon:
            print ("The point lies on the y - axis")
    # if x == 0 and y == 0:
    #     print ("The point lies on the origin.")
    # elif x==0  and y!=0:
    #     print ("The point lies on the x - axis.")
    # elif y==0 and x!=0:
    #     print ("The point lies on the y - axis.")
    elif x > 0 and y > 0:
        print ("It lies in the first quadrant.")
    elif x > 0 and y < 0:
        print ("It lies in the fourth quadrant.")
    elif x < 0 and y > 0: 
        print ("It lies in the second quadrant.")
    else:
        print ("It lies in the third quadrant.")