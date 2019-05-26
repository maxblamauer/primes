 # I, Maxwell Blamauer, 000760618 certify that all code submitted is my own work;
 # that I have not copied it from any other source.
 # I also certify that I have not allowed my work to be copied by others.

# GET an integer larger than 2
# Repeat until the user enters an integer larger than 2
userInput = "0"
while ( int( userInput ) <= 2 ):
    userInput = input( "Please enter an integer greater than 2: " )

#SET user input to n as stated in the assignment instructions
n = int( userInput )

#SET a list of integers as stated in the assignment instructions
i = 2
intList = []
while( i <= n ):
    intList = intList + [ i ]
    i = i + 1

#SET a variable called current to 2 as stated in the assignment instructions
current = 2

#LOOP WHILE current is less than n
    # SET variable p to 0 for tracking the list
        #LOOP WHILE p is less than length of intList
        #IF current is a multiple and not equal to current
        #INCREASE p by 1

i = 0
while ( current < n ):
    p = 0
    while ( p < len( intList ) ):
        if ( current != intList[ p ] and intList[ p ] % current == 0 ):
            intList.remove( intList[ p ] )
        p = p + 1 
    i = i + 1
    current = intList[ i ]
print( intList )
