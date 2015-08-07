################################################
### Daily Programmer Challenge 226 [Easy]    ###
### Source: /r/dailyprogrammer on Reddit.com ###
################################################
'''
August 6, 2015
This program allows a user to input a number of fractions, then adds the fractions
together and returns the sum in simplified fraction form.
'''

# Ask the user how many fractions they would like to add.
print "How many fractions?"
N = int(raw_input(">"))

# Initialize numerator and denominator vectors
nums = []
dens = []

# User inputs fractions, append numerator and denominator to vectors. 
print "Input %d fractions:\n" % N

for i in range(0,N):
    f = raw_input(">").split('/')
    nums.append(int(f[0]))
    dens.append(int(f[1]))

# Find the LCD of the denominators: LCD = product/GCD or (a/GCD)*b to avoid overflow.

# Greatest common divisor function - uses Euclidean Algorithm
def gcd(a,b):
    while b:
        a,b = b,a%b
    return(a)    

# Find the LCD of the denominators: LCD = product/GCD or (a/GCD)*b to avoid overflow.
def LCD(a,b):
   return((a/gcd(a,b))*b)

# Find the LCD of multiple denominators.   
currentLCD = LCD(dens[0], dens[1])

if N>2:
    for i in range(2, N):
        currentLCD = LCD(currentLCD, dens[i])        
finalDen = currentLCD        

# Calculate the numerators of the new fractions to be added
newNums = [a*(currentLCD/b) for a,b in zip(nums, dens)]

# Calculate the sum of numerators
finalNum = sum(newNums)

'''
Simplify the final numerator and denominator by repeatedly dividing by 
the greatest common divisor.
'''

GCD = gcd(finalNum, finalDen)
    
while GCD > 1:
    finalNum = finalNum/GCD
    finalDen = finalDen/GCD
    GCD = gcd(finalNum, finalDen)

# Print final output
print '{}/{}'.format(finalNum, finalDen)
