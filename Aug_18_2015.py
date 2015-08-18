
#####################################
### Daily Programmer 228 Easy     ###
### Letters in Alphabetical Order ###
#####################################
'''
This program takes a word as input, and then tells the user whether the letters
in the word occur in alphabetical order or not. 
'''
# input word
word1 = "almost"

#### Method 1 ####
def alphaWordV1(word):
    length = len(word)
    word_letters = list(word.lower())

    # The ord() function gives us the int value of the character. 
    word_numbers = [ord(a) for a in word_letters]

    # Calculate differences between each pair of letters
    differences = [x-y for x,y in zip(word_numbers[1:length], word_numbers[0:(length-1)])]

    # Check for positive or negative differences
    increasing = not(any(n < 0 for n in differences))
    decreasing = not(any(n > 0 for n in differences))

    if increasing:
        print "%s IN ORDER" % word
    elif decreasing:
        print "%s IN REVERSE ORDER" % word
    else:
        print "%s NOT IN ORDER" % word
        
alphaWordV1(word1)  
    
#### Method 2 ####
    
def alphaWordV2(word):
    if word == "".join(sorted(word)):
        print "%s IN ORDER" % word
    elif word == "".join(list(reversed(word))):
        print "%s IN REVERSE ORDER" % word
    else:
        print "%s NOT IN ORDER" % word
        
alphaWordV2(word1)