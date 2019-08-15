'''
This quizzes the user on U.S. states. All the user has to do is enter every state he/she
can think of. Think Sporcle. When he/she gives up, he/she enters "GIVEUP".
'''

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
right = []

def check(inp):
	inp = inp.title()
	if inp in states:
		print(f'{inp} is indeed a state.')
		states.remove(inp)
		right.append(inp)
	elif inp in right:
		print(f'You said {inp} already.')
	else:
		print('Nope.')

def end_game():
	print(f'You got {len(right)} out of 50 states. ({len(right)/50*100}%)')
	print("Here's the states you missed:")
	for state in states:
		print(state)

start = input('Welcome to the U.S. States Quiz. You simply enter in U.S. states until you either give up or name all of them. To give up at any time, enter GIVEUP. Got it? ')
while True:
	guess = input('Enter in a state. (Enter GIVEUP to give up) ')
	if guess.lower() == 'giveup':
		end_game()
		break
	check(guess)
	if len(states) == 0:
		print('You got all 50 states! Nice work!')
		break
	print(f'You have {len(states)} states left.')