from random import *
while True
    x = randint(1,6)

    y = int(input("Your bet: "))

    while 1 <= y <=6 :
        if y == x:
            print ("The dice value is ", x , ". You win")
        else:
            print ("The dice value is ", x , ". You lose")
        break