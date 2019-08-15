'''
This gives decimal values for the limit, derivative, or integral of a function. Originally, this
was three different programs. I decided to combine these into one.
How it works: I input whether I am finding the limit, derivative, or integral of a function.
I then input the function. If I am finding the limit, I input the value it is approaching.
If I am finding the derivative, I input the point at which I am finding it. If I am finding
the integral, I input the bounds.
'''

from math import log,factorial,e,sqrt,sin,cos,tan,asin,acos,atan,pi

def ln(num):
	return log(num)

def limit(a):
	x = a
	try:
		lim = round(eval(f),3)
	except:
		x += 0.00000000001
		lim = round(eval(f),3)
	return lim

def derivative(a):
	#the derivative of f(x) is the lim as h-->0 of (f(x+h)-f(x))/h
	h = 0.00000000001
	x = a
	y1 = eval(f)
	x += h
	y2 = eval(f)
	deriv = round((y2-y1)/h,3)
	return deriv

def integral(a,b):
	#the integral of f(x) between a and b is lim as n-->∞ of sum of i=1 to n of f(ci)∆xi
	n = 100000
	delt = (b-a)/n
	area = 0
	i = 0
	while i < n:
		x = a + delt*i
		area += eval(f)*delt
		i += 1
	area = round(area,3)
	return area

#display instructions
inst = open('calcinst.txt','r')
message = inst.read()
print(message)
inst.close()

while True:
	m = input('What are you aiming to find? (enter LIM for limit, DER for derivative, INT for integral, QUIT to quit) ')
	m = m.lower()
	if m == 'quit':
		break
	f = input('What is the function? ')
	if m == 'lim':
		val = int(input('What x-value is the limit approaching? '))
		print(f'The limit of {f} as x approaches {val} is {limit(val)}')
	if m == 'der':
		val = int(input('At what value do you want to find the derivative? '))
		print(f'The derivative of {f} with respect to x at x = {val} is {derivative(val)}')
	if m == 'int':
		val1 = int(input('What is the first bound of the integral? '))
		val2 = int(input('What is the second bound of the integral? '))
		print(f'The integral of {f} from x = {val1} to x = {val2} is {integral(val1,val2)}')