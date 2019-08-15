'''
This is yet another program I made for fun. It takes a phrase and prints the letters very
fancily.
Example input: test
Example output:
ooooo ooooo ooooo ooooo 
  o   o     o       o   
  o   oooo  ooooo   o   
  o   o         o   o   
  o   ooooo ooooo   o 
'''

lines = ['ooooo','oooo ','ooo  ','o    ','o   o',' ooo ','  o  ','o ooo','    o','o  o ','oo oo','o o o','oo  o','o  oo','   oo',' o o ',' o   ','   o ','     ']
letters = {'A':[5,4,0,4,4],'B':[1,4,0,4,1],'C':[0,3,3,3,0],'D':[1,4,4,4,1],'E':[0,3,1,3,0],'F':[0,3,1,3,3],'G':[0,3,7,4,0],'H':[4,4,0,4,4],'I':[0,6,6,6,0],'J':[8,8,8,4,5],'K':[4,9,2,9,4],'L':[3,3,3,3,0],'M':[4,10,11,4,4],'N':[4,12,11,13,4],'O':[0,4,4,4,0],'P':[0,4,0,3,3],'Q':[0,4,4,0,14],'R':[0,4,0,9,4],'S':[0,3,0,8,0],'T':[0,6,6,6,6],'U':[4,4,4,4,0],'V':[4,4,4,15,6],'W':[4,4,11,10,4],'X':[4,15,6,15,4],'Y':[4,15,6,6,6],'Z':[0,17,6,16,0],' ':[18,18,18,18,18]}

def print_phrase(phrase):
	for num in range(5):
		line = ''
		for char in phrase:
			line+=lines[letters[char.upper()][num]]+' '
		print(line)

print('You can exit at any time by entering the word QUIT.')
while True:
	inp = input('Enter a phrase to print. ')
	if inp.lower() == 'quit':
		break
	try:
		print_phrase(inp)
	except:
		print('Please enter valid alphabetical characters.')