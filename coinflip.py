#This simulates coin flips (hint: there are no actual coins).

from random import randint
def coinFlip(num):
	heads = 0
	tails = 0
	for _ in range(num):
		rand = randint(1,2)
		if rand == 1:
			print('The coin landed on heads.')
			heads+=1
		else:
			print('The coin landed on tails.')
			tails+=1
	print(f'The coins landed on heads {heads} times.')
	print(f'The coins landed on tails {tails} times.')
while True:
	try:
		coinFlip(int(input('How many times would you like to flip a coin? ')))
		break
	except:
		print('Please enter an integer.')