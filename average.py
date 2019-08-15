'''
This calculates both my unweighted and weighted average. This is one of the only ones that
I made purely out of practicality.
How it works: I input my unweighed grade for each class. I get back my averages.
Example output:
Weighted Average: 101.12 (101)
Unweighted Average: 99.999999 (100)
'''

#data (changes year by year)
classes = [['AP Calc BC',1.1],['AP Computer Science',1.1],['AP Statistics',1.1],['AP Physics II',1.1],['AP Research',1.1],['Race Relations H',1.04],['Engineering 2H',1.04],['Religion IV',1.00]]

#find the averages
unw = 0
w = 0
exempt = 0
for cl in classes:
	try:
		grade = int(input(f'What do you have in {cl[0]}? '))
	except:
		exempt += 1
	else:
		unw += grade
		w += grade*cl[1]
unw /= len(classes)-exempt
w /= len(classes)-exempt
print(f'Weighted Average: {w} ({int(round(w,0))})')
print(f'Unweighted average: {unw} ({int(round(unw,0))})')