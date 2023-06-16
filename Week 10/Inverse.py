for i in range(-10,11,1):
    try:
        print(round(1/i,3) )
    except ZeroDivisionError:
        print ("Infinity")
        
