import math

number_of_days = float(input("Please input the number of days: "))

# find the number of days
days = number_of_days//1

#find the number of hours
number_of_hours = (number_of_days - days) * 24 
hours = number_of_hours // 1

#find the number of minutes
number_of_minutes = (number_of_hours - hours) * 60
minutes  = number_of_minutes//1

# find the number of seconds
seconds = round((number_of_minutes - minutes) *60, 4)

print (number_of_days , " days = ", days , "days" , hours, "hours", minutes, "minutes" , seconds, "seconds")
