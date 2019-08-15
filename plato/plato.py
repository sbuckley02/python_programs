'''
In AP English Language and Composition, I once had a multi-part assignment on a Plato passage in
which one of the parts contained the following question: "Identify the shortest sentence of the
passage and explain the importance of the message it conveys. Identify the longest sentence in the
passage and explain the value of the detail it conveys."
Since I demand perfection, I created this computer program, which identifies these sentences from
a text file with the passage and outputs them.
'''

f = open('platotext.txt','r')
text = f.read()
f.close()
text = text.split('.')
text.pop(len(text)-1)
short = text[0]
longest = text[0]
for index,sen in enumerate(text):
	if len(sen) < len(short):
		short = text[index]
	if len(sen) > len(longest):
		longest = text[index]
print(f'The longest sentence is {longest}.')
print(f'The shortest sentence is {short}.')