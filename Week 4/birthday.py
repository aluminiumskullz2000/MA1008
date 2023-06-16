import math

while True:
    day1 = int (input ("Please input the day of the first person's birthday: "))
    month1 = int(input ("Please input the month of the first person's birthday: "))
    year1 = int(input ("Please input the year of the first person's birthday: "))
    day2 = int(input ("Please input the day of the second person's birthday: "))
    month2 = int(input ("Please input the month of the second person's birthday: "))
    year2 = int(input ("Please input the year of the second person's birthday: "))

    if year1 > year2:
        print ("Person 1 is older than Person 2")
    elif year2 > year1:
        print ("Person 2 is older than Person 1")
    else:
        if month1 > month2:
            print ("Person 1 is older than Person 2")
        elif month2 > month1:
            print ("Person 2 is older than Person 1")
        else:
            if day1 > day2:
                print ("Person 1 is older than Person 2")
            elif day2 > day1:
                print ("Person 2 is older than Person 1")
            else:
                print("They are of the same age")