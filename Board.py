"""Battship game in Python - Codeacademy"""

#import randint function from the the random module
from random import randint

#create a 5x5 board of "O"
board = []
for loop in range (0,4):
	board.append(["O"] * 5)

#simple function to print the board
def print_board(board):
	for i in board:
		print " ".join(board[i]) """us the join function to combine items in string"""

#hide our battleship in a random location on the board.
def random_row(board):
	return randint(0, len(board) - 1)
def random_col(board):
	return randint(0, len(board) - 1)

#coordinates for the ship
ship_row = random_row(board)
ship_col = random_col(board)

#debugging - print location of the ship. Comment out later
"""print "Row: " + str(ship_row) + ", " + "Column: " + str(ship_col)"""

#use the raw_input function to allow player to guess the row/column of the battleship
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Column: "))

#check to see if the player guessed right.
if guess_row == ship_row and guess_col == ship_col:
	print "Congratulations! You sank my battleship!"
#player enters location that is not on the board
elif (guess_row, guess_col) not in range(len(board)):    
	#debug
	"""print len(board)"""    
	print "Oops, that's not even in the ocean."
#player enters location that has already been guessed
elif board[guess_col][guess_row] == "X":    
	print " You guessed that one alread."
else:
	board[guess_row][guess_col] = "X"
	#debugging - print location of missed guess
	print_board(board) 
	"You missed my battleship!"


