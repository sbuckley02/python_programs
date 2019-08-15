'''
This contains a function which uses another program of mine (basechanger.py) to convert decimal
numbers into binary.
'''

from basechanger import convert_to_base

def text_to_bin(text):
	new = ''
	for char in text:
		new = new + convert_to_base(ord(char),2) + ' '
	return new