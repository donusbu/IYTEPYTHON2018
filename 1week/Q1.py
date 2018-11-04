print( 'Hello World' )  #print is a function 'Hello world' is a string
## ----------------- is a comment
number = 2  # this is variable named 'number' hold a number
numara = 5
ahmet = 'This is a string'
first_string = "How are you"  # hold string
print( first_string )
print( number + numara )
print( number - number )
print( number * numara + number )
print( numara / number )
print( first_string + ahmet )
numara = 10
print( numara )
numara = 15
print( numara )
numara1 = 20

numara = numara1
print( numara )
numara = numara + 8
numara += 4
print( numara )

numara = "Bu bir numaradir"
print( numara )


boolean = True
integer = 5
float_ = 5.6
array = [4, 5, 6, 7, 8]
dict = {'key': 'value'}
tuple_ = (4, 5, 6, 7)


number = 9
text = 'this is text'
print( number == 4 )
print( number + 2 != 8 )
print( number < 8 )
print( number <= 8 )
print( number > 8 )
print( number >= 8 )
print( text == 'this is text' )
print( text == 'merhaba' )
print( 'is' in text )

import math

number = 7
sqrt_number = math.sqrt( number )
sqrt_number = math.sqrt( sqrt_number )

sqrt_number_2 = math.sqrt( math.sqrt( number ) )

print( sqrt_number, sqrt_number_2 )

number = '46'
print(number.isdigit())
string = 'This is a string'
print( string.upper() )
print( string.lower() )
print( string.replace( 'This', 'That' ) )
print( len( string ) )
print( string.upper().split( ' ' ) )
print( ''.join( reversed( string ) ) )