'''
This is my favorite Python program I have made. It's a game in which you can play games of
Blackjack to acquire coins.
How it works: You start off with 100 coins. After, you can bet coins on games of Blackjack.
You can only bet what you have, so you cannot go into debt. You can end the game whenever
you wish.
'''

from deck import cards
from random import randint

coins = 100
inp = None
userTotal = None
compTotal = None


def newCard():
	while True:
		rand = randint(0,51)
		if cards[rand].used == False:
			cards[rand].used = True
			return cards[rand]

def clear():
	for num in range(0,50):
		print('')

def start():
	global inp
	clear()
	inp = input("Welcome to blackjack. If you don't know how to play, look it up on Google. \
You will start off with 100 coins. Enter QUIT at any time to end the game \
and finalize the amount of coins you have accumulated. Anything else that is \
entered will automatically continue the game. \nContinue ")
	if inp.upper() == 'QUIT':
		endGame()
	else:
		playGame()

def endGame():
	global coins
	clear()
	inp2 = input(f'You finished with {coins} coins.\nPlay again? (Enter YES to play, NO to not play) ')
	if inp2.upper() == 'YES':
		coins = 100
		start()
	else:
		clear()
		print(f'Seems like you were satisfied with {coins} coins.')

def playGame():
	global inp,coins,userTotal,compTotal
	clear()
	while True:
		inp = input('How much would you like to wager? ')
		if inp.upper() == 'QUIT':
			endGame()
			return
		else:
			try:
				wagered = int(inp)
			except:
				print('Please enter a number')
				continue
			if wagered < 0:
				print("You can't enter a negative number.")
				continue
			if wagered <= coins:
				break
			print(f'You have {coins} coins. That is the max that you can bid.')
	clear()
	userCards = [newCard(),newCard()]
	compCards = [newCard(),newCard()]
	def printUserCards():
		print('Your cards:')
		for card in userCards:
			print(card)
	while True:
		userTotal = 0
		printUserCards()
		print("Dealer's (computer's) cards:")
		print(compCards[0])
		print(' _____\n|     |\n|     |\n|     |\n|     |\n|     |\n  ̅̅̅̅̅')
		for card in userCards:
			if card.kind == 'A':
				card.value = int(input('Would you like your ace (or one of your aces) to have a value of 1 or 11? '))
			userTotal+=card.value
		if userTotal == 21:
			inp = input("You have reached 21. It is now the dealer's turn. (Enter anything) ")
			if inp.upper() == 'QUIT':
				endGame()
				return
			break
		elif userTotal > 21:
			print("You have busted. You lose.")
			coins-=wagered
			playAgain()
			return
		inp = input('Hit or stand? ')
		if inp.upper() == 'HIT':
			userCards.append(newCard())
			continue
		elif inp.upper() == 'STAND':
			inp = "It is now the dealer's turn. (Enter anything) "
			if inp.upper() == 'QUIT':
				endGame()
				return
			break
		elif inp.upper() == 'QUIT':
			endGame()
			return
		else:
			print('Please enter either HIT or STAND.')
	def printCompCards():
		print("Dealer's (computer's) cards:")
		for card in compCards:
			print(card)
	def findComp():
		global compTotal
		compTotal = 0
		for card in compCards:
			compTotal+=card.value
	findComp()
	printUserCards()
	print(f'Your total value: {userTotal}')
	while compTotal < 17:
		for card in compCards:
			if card.kind == 'A':
				card.value = 11
				findComp()
				if compTotal > 21:
					card.value = 1
				break
		printCompCards()
		print('The dealer draws a card.')
		compCards.append(newCard())
		findComp()
	printCompCards()
	print(f"The dealer's total value: {compTotal}")
	if compTotal > 21:
		print('The dealer has busted. You win.')
		coins+=wagered
	elif compTotal < userTotal:
		print('You win.')
		coins+=wagered
	elif compTotal > userTotal:
		print('You lose.')
		coins-=wagered
	else:
		print('You tied.')
	playAgain()
def playAgain():
	for card in cards:
		card.used = False
	print(f'Coins: {coins}')
	inp = input('Play another round of blackjack? (Enter YES to play, NO to end the game) ')
	if inp.upper() == 'NO' or inp.upper() == 'QUIT':
		endGame()
	else:
		clear()
		print(f'You have {coins} coins.')
		playGame()

start()