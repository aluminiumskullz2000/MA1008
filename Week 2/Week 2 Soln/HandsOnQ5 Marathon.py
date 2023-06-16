# Hands-on Q5: Marathon

TotalDist = 42.2
TimeFirst12km = 12.0/15
TimeNext15km = 15.0/10
TimeNext10km = 10.0/14
Remainingkm = 42.2-12-15-10
TimeRemainingkm = Remainingkm/18

TotalTime = TimeFirst12km + TimeNext15km + TimeNext10km + TimeRemainingkm

print("The total time taken is ", TotalTime, "hours.")

# Express the time in hours, minutes, seconds
Hours = int(TotalTime)
HourFraction = TotalTime - Hours
Minutes = int(HourFraction*60)
MinuteFraction = HourFraction*60 - Minutes
Seconds = MinuteFraction*60

print("which is ", Hours, "hours", Minutes, "minutes and", Seconds, "seconds")
