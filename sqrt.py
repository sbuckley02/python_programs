#This finds the square root of a number without using the math.sqrt() function

def root(num):
	att = 45
	for _ in range(500):
		att = 0.5*(att+(num/att))
	return att

while True:
	inp = input('Enter a number. ')
	if inp == 'quit':
		break
	else:
		print(f'The square root is {root(int(inp))}')