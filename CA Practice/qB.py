# A population survey divides people into four age groups:
# Senior: 60 years and above.
# Adult: between 21 and 59, inclusive.
# Youth: between 11 and 20, inclusive.
# Child: less than 11 years old.
# Write a program that reads in the ages of people. Keep on reading until a negative age is
# given, at which point you should terminate the input. Your program should reject any age
# higher than 115, and require the user to provide it again.
# After input, print the total number of people and the number in each category. At the end,
# also print the average age of the people and the group this average belongs to.
# Here is an example dialogue (underlined text is user input):
# Enter age of Person 1: 69
# Enter age of Person 2: 10
# Enter age of Person 3: 28
# Enter age of Person 4: -1
# Input completed.
# Number of people: 3
# Number of seniors: 1
# Number of adults: 1
# Number of youths: 0
# Number of children: 1
# The average person is at age 35.67, adult
# (Note: The example above has only three people. The actual number can be many more, possibly thousands. 
# Your program should allow that.)


positive = True
persons = 1
seniors = 0
adults = 0
youths = 0
children = 0
ages = 0

while positive:
    age = int (input("Enter age of Person{:2.0f}:".format(persons)))    
    if age < 11 and age >= 0 :
        children += 1
        ages += age
        persons += 1
    elif age >= 11 and age <= 20:
        youths += 1
        ages += age
        persons += 1
    elif age >= 21 and age <= 59:
        adults += 1
        ages += age
        persons += 1
    elif age >= 60:
        seniors += 1
        ages += age
        persons += 1
    else: 
        positive = False
        print ("Input completed")
        print ("Number of people = {:d}".format(persons-1))
        print ("Number of seniors = {:d}".format(seniors))
        print ("Number of adults = {:d}".format(adults))
        print ("Number of youths = {:d}".format(youths))
        print ("Number of children = {:d}".format(children))
        averageage = ages/(persons-1)
        if averageage < 11 and averageage >= 0 :
            print ("The average person is at age {:.2f}, children.".format(averageage))
        elif averageage >= 11 and averageage <= 20:
            print ("The average person is at age {:.2f}, youth.".format(averageage))            
        elif averageage >= 21 and averageage <= 59:
            print ("The average person is at age {:.2f}, adult.".format(averageage))
        elif averageage >= 60:
            print ("The average person is at age {:.2f}, children.".format(averageage))