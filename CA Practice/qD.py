# If we know which day of the week the first of a month is, then we can generate the month’s
# calendar in one page. Write a program to read in the day of the week for the first of the month
# and print the month’s calendar. You can use numbers to represent the days of the week (1 for
# Monday, 2 for Tuesday, etc.). You can also assume you know the number of days in the month,
# say 30 days. Here is an example dialogue (underlined text is user input):
# Which day of the week is the first of the month? 4
# The calendar:
# Mon Tue Wed Thu Fri Sat Sun
#  1 2 3 4
#  5 6 7 8 9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30

first = int(input("Which day of the week is the first of the month?"))
counter = 0

print ("Mon Tue Wed Thu Fri Sat Sun")
print ("    "*(first-1), end="")
for i in range (1,31,1):
    counter +=1
    print ("{:>3.0f}".format(i), end=" ")

    if (counter+first-1) % 7 == 0:
        print()



