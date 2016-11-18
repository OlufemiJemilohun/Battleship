#

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
