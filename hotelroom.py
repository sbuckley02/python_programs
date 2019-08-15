'''
I was in Europe with some people and I shared a room with three others. There were a few
sleeping options, and some were clearly better than others. To decide who would get their
preferred sleeping option, and in which order, I created this program.
How it worked: The program generated a random number between 1 and 10. We took turns guessing,
until someone got the number. Until the order was set, the program repeated this.
'''

#these you change
names = ['Buckley','Conor','Cregin','Chris']
firstnum = 1
lastnum = 10

#this you don't change
prefixes = ['first','second','third','fourth','fifth']
turn = 0

from random import randint

orderednames = []
end = len(names)-1
while end >= 0:
	rand = randint(0,end)
	orderednames.append(names[rand])
	names.pop(rand)
	end += -1

def update_turn():
	global turn
	if turn == len(orderednames)-1:
		turn = 0
	else:
		turn += 1

def complete_round(prefix):
	global orderednames
	num = randint(firstnum,lastnum)
	while True:
		if int(input(f'{orderednames[turn]}, what is the {prefix} number? (between {firstnum} and {lastnum}) ')) != num:
			print('WRONG')
		else:
			print(f'{orderednames[turn]}, you got it')
			orderednames.pop(turn)
			break
		update_turn()

for n in range(len(orderednames)-1):
	complete_round(prefixes[n])
	turn = 0