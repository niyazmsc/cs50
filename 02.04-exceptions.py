import sys


try:
    x = int( input("x: ") )
    y = int( input("y: ") )
except ValueError:
    print( "Invalid Input." )
    sys.exit(1)


# result = x/y

try: 
    result = x/y
except ZeroDivisionError:
    print( "Can not divide by zero." )
    sys.exit( 1 )

print( f"{x}/{y} = {result} " )
