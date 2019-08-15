'''
Near the end of one of my AP Calculus AB classes, my teacher gave us a riddle.
The following is from Wikipedia (this isn't a research essay):
"People are standing in a circle waiting to be executed. Counting begins at a specified
point in the circle and proceeds around the circle in a specified direction. After a
specified number of people are skipped, the next person is executed. The procedure is
repeated with the remaining people, starting with the next person, going in the same direction
and skipping the same number of people, until only one person remains, and is freed.
The problem... is to choose the position in the initial circle to avoid execution."

When my teacher gave us the riddle, he told us that only 1 person would be skipped each turn.
He wanted us to solve the resulting riddle mathematically. However, I thought "a computer
can probably solve this much quicker than I can".
I then made this, which returns the position in which one would survive in.
'''

def find_position(n):
	numbers = []
	for num in range(n):
		numbers.append(num+1)
	index = 1
	while len(numbers)>1:
		numbers.pop(index)
		index+=1
		if index == len(numbers):
			index = 0
		elif index == len(numbers)+1:
			index = 1
	return numbers[0]