'''
This is a 2-player Tic-Tac-Toe game. Players input the number of the box they
want to place an X or O in.
'''

board = []
turns = 0
gameOver = False
def clear_output():
	#clear the terminal window
	for num in range(0,50):
		print('')
def startUp():
	#executes before a game is played
	clear_output()
	q1 = input('Welcome to Tic Tac Toe\nEnter YES to play ').upper()
	if q1 == 'YES':
		clear_output()
		print('To play, input the number of the box you want to place your X or O (1-9, going from the top left to the bottom\nright) in the input asking for it.')
		q2 = input('Got it?(type YES) ').upper()
		if q2 == 'YES':
			clear_output()
			startGame()
def startGame():
	#executes when the game starts
	global p1, p2, board, turns, gameOver
	board = [" "," "," "," "," "," "," "," "," "]
	turns = 0
	gameOver = False
	printBoard()
	playGame()
def playGame():
	#this combines other functions/variables to play the game
	while gameOver == False:
		askForInput()
		checkIfFull()
		checkIfOver()
	endQuest = input('Play again?(type YES) ').upper()
	if endQuest == 'YES':
		startUp()
	else:
		clear_output()
def checkIfOver():
	#contains a bunch of checks
	check(0,1,2)
	check(3,4,5)
	check(6,7,8)
	check(0,3,6)
	check(1,4,7)
	check(2,5,8)
	check(0,4,8)
	check(2,4,6)
def check(ind1,ind2,ind3):
	#check if three boxes are all Xs or all Os and end the game if so
	global gameOver
	if board[ind1] == 'X' and board[ind2] == 'X' and board[ind3] == 'X':
		gameOver = True
		print('Player 1 (X) Wins!')
	elif board[ind1] == 'O' and board[ind2] == 'O' and board[ind3] == 'O':
		gameOver = True
		print('Player 2 (O) Wins!')
def checkIfFull():
	#checks if the board if completely full, if not, the game is over
	global gameOver
	gameOver = True
	for box in board:
		if box == " ":
			gameOver = False
			break
def printBoard():
	#display the current board to the user
	clear_output()
	print(f'{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}')
def askForInput():
	#get the user's input
	global turns
	if turns%2 == 0:
		p1inp = int(input('Player 1, enter a number from 1-9 (you are X)'))
		for index,box in enumerate(board):
			if box == " " and index == p1inp-1:
				board[index] = 'X'
	else:
		p2inp = int(input('Player 2, enter a number from 1-9 (you are O)'))
		for index,box in enumerate(board):
			if box == " " and index == p2inp-1:
				board[index] = 'O'
	turns+=1
	printBoard()
startUp()