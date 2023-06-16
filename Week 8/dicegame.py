from random import *

def rolldiceonce():
    value = randint(1,6)
    return value

def rollthreetimes():
#can use global as well global x, global y, global z, global sum
    x = rolldiceonce()
    y = rolldiceonce()
    z = rolldiceonce()
    if x == y  and y == z:
        print ("The three values are the same")
    sum = x + y + z
    return sum , x , y, z

def bigorsmall():
    x,y,z,sum = rollthreetimes()
    if x == y  and y == z:
        print ("Jackpot!")
    elif sum >= 11:
        print ("Big")
    else:
        print ("Small")

