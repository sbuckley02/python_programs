'''
This converts the user's input, an integer, into words.
Example input: 123456789
Example output: 123456789 = one hundred twenty-three million
four hundred fifty-six thousand seven hundred eighty-nine
'''

def convert(num):
	#converts an integer into words
	final = ''
	if num == 0:
		return 'zero'
	if num < 0:
		neg = 'negative '
		num*=-1
	else:
		neg = ''
	num = str(num)
	ones = {'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
	teens = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
	tens = {'20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
	groups = {'16':'quadrillion','13':'trillion','10':'billion','7':'million','4':'thousand'}
	presets = [ones,teens,tens]
	def returnHundred(n):
		hund = ''
		for l in presets:
			for key in l.keys():
				if n == key:
					return l[key]
				if len(key) == 2:
					if n[-1] == key[-1] and n[-2] == key[-2]:
						hund+=l[key]
				elif n[-1] == key[-1] and n[-2] == '0':
					hund+=l[key]
		if int(n[-2]) > 1 and n[-1] != '0':
			for key in tens.keys():
				if n[-2]+'0' == key:
					hund += tens[key]
			for key in ones.keys():
				if n[-1] == key:
					hund+='-'+ones[key]
		if len(n) == 3:
			for key in ones.keys():
				if key == n[-3]:
					hund = ones[key]+' hundred '+hund
		return hund
	for key in groups.keys():
		if len(num) >= int(key) and str(num[:-int(key)+1]) != '000':
			final+=returnHundred(num[:-int(key)+1])+' '+groups[key]+' '
			num = num[-int(key)+1:]
		elif len(num) >= int(key):
			num = num[-int(key)+1:]
	final+=returnHundred(num)
	return neg+final


def askForInput():
	while True:
		try:
			n = input('Enter an integer to get back its name. Enter QUIT to quit. ')
			if n.lower() == 'quit':
				break
			else:
				n = int(n)
		except:
			print('Please enter a valid integer.')
		else:
			print(f'{n} = {convert(n)}')
askForInput()