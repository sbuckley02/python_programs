'''
This is another one I made for fun. The user inputs an integer and the program gives a string
of that number random letters.
Example input: 5
Example output: snctp
'''


from random import randint

def make_string(length):
	final = ''
	for _ in range(length):
		rand = randint(97,122)
		final+=chr(rand)
	return final

print(make_string(int(input('How long will the random string be? '))))