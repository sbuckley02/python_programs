#This checks if an email is valid.

import re

mail = input('Type in an email ')
match = re.search("\w+@+\w", mail) #check for a letter followed by an @ followed by a letter

if match:
	match2 = re.search("\w\.\w",mail) #check for a letter followed by a . followed by a letter
	if match2:
		print("That's an email.")
	else:
		print("No, that is not an email.")
else:
	print("No, that is not an email.")