#create a 5x5 board of "O"
board = []
for loop in range (0,4):
	board.append(["O"] * 5)

#simple function to print the board
def print_board(board):
	for i in board:
		print " ".join(board[i]) """us the join function to combine items in string"""

