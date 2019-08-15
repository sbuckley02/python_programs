'''
Given an integer, this tells the user how many steps it takes to turn the integer into 1
using the Collatz conjecture.
'''

def findSteps(num):
	steps = 0
	while num != 1:
		if num%2 == 0:
			num/=2
		else:
			num = num*3 + 1
		steps+=1
	return steps

while True:
	try:
		n = int(input('Please enter an integer. '))
	except:
		print("You didn't enter an integer.")
	else:
		print(f'It took {findSteps(n)} steps to turn {n} into 1.')
		break