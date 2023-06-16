number = input ("Please key in something: ")


try:
    int(number)
    print ("is an integer")
except ValueError:
    try:
        float(number)
        print("is a float")
    except ValueError:
        print ("is a string")

