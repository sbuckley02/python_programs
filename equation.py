'''
This contains a function which returns the linear equation, in y = mx + b form,
of two coordinates given.
Example input: (1,3),(4,9)
Example output: y = 2.0x + 1.0
'''

def findEquation(coord1,coord2):
	slope = (coord2[1]-coord1[1])/(coord2[0]-coord1[0])
	newCoord = [coord1[0],coord1[1]]
	while newCoord[0] > 1:
		newCoord[0]-=1
		newCoord[1]-=slope
	while newCoord[0] < 1:
		newCoord[0]+=1
		newCoord[1]+=slope
	yint = newCoord[1]-slope
	print(f'y = {slope}x + {yint}')