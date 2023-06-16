import math

Distance1 = float ( input ("Distance 1 = "))
Speed1 = float ( input ("Speed 1 = "))
Distance2 = float ( input ("Distance 2 = "))
Speed2 = float ( input ("Speed 2 = "))
Distance3 = float ( input ("Distance 3 = "))
Speed3 = float ( input ("Speed 3 = "))
Speed4 = float ( input ("Speed 4 = "))

Distance4 = (42.2 - Distance1 - Distance2 - Distance3)
Distance4 = round(Distance4, 3)

Total_time= (Distance1/Speed1 + Distance2/Speed2 + Distance3/Speed3 +Distance4/Speed4)
Total_time = round(Total_time, 3)

print ("Remaining Distance is ", Distance4)
print ("Total time taken to run the marathon is ", Total_time)
