#create a 5x5 board of "O"
board = []
for loop in range (0,4):
	board.append(["O"] * 5)

#function to print the board
def print_board(board):
	for i in board:
		print board[i]

