
########################################################
### Daily Programmer 226 Intermediate - Connect Four ###
########################################################

# Source: r/dailyprogrammer

'''
This program tracks the progress of a game of connect-four, checks for a winner, then outputs 
the number of moves and position of four winning pieces.
'''
import pandas as pd
from pandas import DataFrame
from math import floor
import sys

### Read in the list of moves from a text file
f = open('226_int_2.txt', 'r')

### Create a game board 
board = DataFrame(index=range(1,7), columns=list('ABCDEFG'))
board = board.fillna('.')

### Initialize next free space and move count dictionaries
next_free_space = {'A':6, 'B':6, 'C':6, 'D':6, 'E':6, 'F':6, 'G':6}
move_count = {'X':0, 'O':0}

### Function that adds a move to the board
def add_move(col, player):
    global board, next_free_space, move_count
    board[col][next_free_space[col]] = player
    next_free_space[col] -= 1
    move_count[player] += 1

### Create our sequences to check for winners
sequences = []
# rows
for i in range(0,6):
    sequences.append(range(7*i, 7+7*i))
# columns
for i in range(0,7):
    sequences.append([7*j + i for j in range(0,6)])
# diagonals   
diag_length = [4,5,6,6,5,4]   
# diagonals right
diags_right = [14,7,0,1,2,3]
for i in range(0,len(diags_right)):   
    sequences.append([8*j + diags_right[i] for j in range(0, diag_length[i])])
# diagonals left
diags_left= [3,4,5,6,13,20]
for i in range(0,len(diags_left)):   
    sequences.append([6*j + diags_left[i] for j in range(0, diag_length[i])])

### Function that changes an index number to coordinates
def num_to_coord(n):
   row = int(floor(n/7))+1
   col = list('ABCDEFG')[n%7]
   return str(col)+str(row)

### Function to be run when a winner is found. Prints number of moves, winning positions and the final board.
def winner_found(player,code, vector, line):
    print "%s is a winner in %d moves!" % (player, move_count[player])
    start = line.find(code)
    for i in range(0,4):
        print num_to_coord(vector[start+i])
    print board
    f.close()
    sys.exit()
       
### Function that checks for winners   
def check_winners():    
    boardList = board.values.flatten()

    for s in sequences:
        check_line = "".join([boardList[i] for i in s])
        if "XXXX" in check_line:
            winner_found('X','XXXX', s, check_line)
        if "OOOO" in check_line:
            winner_found('O','OOOO', s, check_line)
##########################################



for line in f:
    next = line.split("  ")
    move_X = next[0]
    move_O = next[1].upper().rstrip()
    
    #Add an X 
    add_move(move_X, 'X')
    check_winners()
    
    #Add an O 
    add_move(move_O, 'O')
    check_winners()

f.close()
print "Nobody won!"


