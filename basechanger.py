#This contains a function that converts decimals to numbers of any base from 2 to 36.

def convert_to_base(num,base):
	values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if base < 2 or base > 36:
		return None
	digits = []
	while num > 0:
		exp = 0
		while base**exp < num:
			exp+=1
		if base**exp > num:
			exp+=-1
		num+=-(base**exp)
		digits.append(exp)
	newnum = ''
	place = digits[0]
	while place >= 0:
		amount = 0
		for dig in digits:
			if dig == place:
				amount+=1
		newnum = newnum+values[amount]
		place+=-1
	return newnum