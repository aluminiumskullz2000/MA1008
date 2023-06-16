import math
##use a dictionary
year = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:30,11:31,12:30}
##use list also can
def noofdays(day,month):
    numberofdays = 0
    while month > 0:
        month -=1
        numberofdays += year[month-1]

    numberofdays += day
    print ("The number of days from 1/1/2019 to {:n}/{:n}/2019 is {:n}".format(day,month,numberofdays))
