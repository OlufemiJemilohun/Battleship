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

#use the raw_input function to allow player to guess the row/column of the battleship
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Column: "))

#Debugging - print location of the ship. Comment out later
print ship_row
print ship_col

#check to see if the player guessed right.
if guess_row == ship_row and guess_col == ship_col:
	print "Congratulations! You sank my battleship!"
else:
	board[ship_row[ship_col]] = "X"
	print_board(board) """debug"""
	"You missed my battleship!"
