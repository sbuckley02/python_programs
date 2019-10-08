'''
I was having a discussion with my family once. We were talking about how it was technically
sexist that whenever a man and a woman get married, the woman has to take the man's last
name. I recognized this, but I also recognized the fact that simply putting a hyphen between
both last names was not ideal. Think about it this way:
A child would have a last name of something-something. If he/she married someone who also had
a hyphenated name, their child would have a last name of something-something-something-something.
Eventually, people would have 256 last names and it would not be pretty.

I then thought of a system that would solve this dilemma: Both parents would input their last names
into a computer program (this). The first part of their last names would be taken (if there is only
one name, that would be the part). Then, a random number, either 0 or 1, is generated. If the number
is 0, one name goes first, is followed by a hypen, and the other name goes second. The opposite
happens if the number is 1.

Here's an example:

Bradley Williams and Shelly Magill have a child named Ted. The program generates a random number of
0, so their child's full name is Ted Williams-Magill.

Ted Williams-Magill and Anna Carter-Johnson have a child named Brooke. The program generates a
random number of 1, so their child's name is Brooke Carter-Williams.

From the example, Shelly's son still had her last name. However, since she was unlucky with the
random number, her name got dropped in the next generation. This is not a perfect solution, but
it gets rid of sexism in naming by making name drops pure luck and allows people's children to
have some/all of both of their parents' names.
'''

from random import randint

one = input('What is the first name? ')
two = input('What is the second name? ')

def simplify(name):
	l = name.split('-')
	name = l[0]
	return name

one = simplify(one)
two = simplify(two)
num = randint(0,1)
if num == 0:
	print(f'The new last name is {one}-{two}.')
else:
	print(f'The new last name is {two}-{one}.')
