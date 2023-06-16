# Get inputs
print( "please input the values" )
a1 = float( input( " a1: " ) )
b1 = float( input( " b1: " ) )
c1 = float( input( " c1: " ) )
a2 = float( input( " a2: " ) )
b2 = float( input( " b2: " ) )
c2 = float( input( " c2: " ) )

# Compute x and y
x = ( b2*c1 - b1*c2 ) / ( a1*b2 - a2*b1 )
y = ( a1*c2 - a2*c1 ) / ( a1*b2 - a2*b1 )

# Report results
print( "x = " , x )
print( "y = " , y )
