import math

# Get radius
radius = input( "input radius: " ) 

# Compute volume
volume = 4.0 / 3.0 * math.pi * radius * radius * radius

# Compute surface area
surface = 4.0 * math.pi * radius * radius

# Report results
print( "sphere volume       = " , volume  )
print( "sphere surface area = " , surface )
