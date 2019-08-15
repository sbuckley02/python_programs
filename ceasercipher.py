'''
This program allows you to encipher or decipher messages using Ceaser's method. This method
involves shifting every letter by the key. For example, "a" shifted by the key of 2 would be
"c". Deciphering does the opposite ("c" becomes "a").
'''

def encipher(string,amount):
	encoded = ''
	for char in string:
		def addToEncoded(min,max):
			if ord(char) >= min and ord(char) <= max:
				newOrd = ord(char)+(amount%26)
				while newOrd < max:
					newOrd+=26
				if newOrd > max:
					newOrd = newOrd%max+()
				encoded+=chr(newOrd)
		if ord(char) >= 65 and ord(char) <= 90:
			newOrd = ord(char)+(amount%26)
			while newOrd < 65:
				newOrd+=26
			if newOrd > 90:
				newOrd = newOrd%90+64
			encoded+=chr(newOrd)
		elif ord(char) >= 97 and ord(char) <= 122:
			newOrd = ord(char)+(amount%26)
			while newOrd < 97:
				newOrd+=26
			if newOrd > 122:
				newOrd = newOrd%122+96
			encoded+=chr(newOrd)
		else:
			encoded+=char
	return encoded
def decipher(string,amount):
	return encipher(string,-amount)
mode = input('Would you like to encipher or decipher something? ').lower()
if mode == 'encipher':
	print(encipher(input('Enter the message to encipher. '),int(input('Enter the key to encipher it with (an integer). '))))
else:
	mode_two = input('Do you know the key? (YES or NO) ').lower()
	if mode_two == 'yes':
		print(decipher(input('Enter the message to decipher. '),int(input('Enter the key to attempt to decipher it with (an integer). '))))
	else:
		message = input('Enter the message to decipher. ')
		for num in range(25):
			print(f'{decipher(message,num+1)} (key = {num+1})')