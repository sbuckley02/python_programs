'''
This one I made for fun. It takes a string and puts spaces between each character.
Example input: This is a sentence.
Example output: T h i s  i s  a  s e n t e n c e .
'''
def print_spaced(string,spacing):
	l = []
	for char in string:
		l.append(char)
		l.append(' '*spacing)
	s = ''.join(l)
	print(s)

while True:
	spacing = input('Enter the amount of spaces between each character. ')
	if spacing.lower() == 'quit':
		break
	else:
		spacing = int(spacing)
		word = input('Enter some word/phrase/something. ')
		if word.lower() == 'quit':
			break
		else:
			print_spaced(word,spacing)