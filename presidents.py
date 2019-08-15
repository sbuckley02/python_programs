'''
This quizzes the user on U.S. presidents. The user has to enter as many presidents as
possible in order (inputs can just be the last name). Think Sporcle.
'''
first = ['George','John','Thomas','James','James','John','Andrew','Martin','William','John','James','Zachary','Millard','Franklin','James','Abraham','Andrew','Ulysses','Rutherford','James','Chester','Grover','Benjamin','Grover','William','Theodore','William','Woodrow','Warren','Calvin','Herbert','Franklin','Harry','Dwight','John','Lyndon','Richard','Gerald','Jimmy','Ronald','George','Bill','George','Barack','Donald']
middle = [None,None,None,None,None,'Quincy',None,None,'Henry',None,'K.',None,None,None,None,None,None,'S.','B.','A.','A.',None,None,None,None,None,'Howard',None,'G.',None,None,'D.','S.','D.','F.','B.',None,None,None,None,'H.W.',None,'W.',None,None]
last = ['Washington','Adams','Jefferson','Madison','Monroe','Adams','Jackson','Van Buren','Harrison','Tyler','Polk','Taylor','Fillmore','Pierce','Buchanan','Lincoln','Johnson','Grant','Hayes','Garfield','Arthur','Cleveland','Harrison','Cleveland','McKinley','Roosevelt','Taft','Wilson','Harding','Coolidge','Hoover','Roosevelt','Truman','Eisenhower','Kennedy','Johnson','Nixon','Ford','Carter','Reagan','Bush','Clinton','Bush','Obama','Trump']

right = 0

for pres in range(45):
	st = str(pres+1)
	if st[0] == '1' and len(st) == 2:
		suff = 'th'
	elif st[-1] == '1':
		suff = 'st'
	elif st[-1] == '2':
		suff = 'nd'
	elif st[-1] == '3':
		suff = 'rd'
	else:
		suff = 'th'
	ans = input(f'Who was the {pres+1}{suff} President of the United States? ').lower()
	if ans == first[pres].lower()+' '+last[pres].lower() or ans == last[pres].lower():
		right+=1
		print('Correct!')
		continue
	try:
		if ans == first[pres].lower()+' '+middle[pres].lower()+' '+last[pres].lower():
			right+=1
			print('Correct!')
			continue
	except:
		pass
	if middle[pres] != None:
		print(f'The {pres+1}{suff} President of the United States is {first[pres]} {middle[pres]} {last[pres]}.')
	else:
		print(f'The {pres+1}{suff} President of the United States is {first[pres]} {last[pres]}.')
print(f'You got {right} out of 45 presidents correct ({round((right/45)*100,2)}%)')