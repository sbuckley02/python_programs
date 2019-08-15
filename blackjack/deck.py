'''
As a part of the blackjack game, this contains every card class and creates objects
(or should I say cards) of these classes. It also puts them into a list for some
reason (bare with me, I made this a long time ago).
'''

class Card():
	def __init__(self,kind,value):
		self.used = False
		self.kind = kind
		self.value = value

class Club(Card):
	def __init__(self,kind,value):
		super().__init__(kind,value)
	def __str__(self):
		if self.kind == '10':
			return ' _____\n|10   |\n|♣︎    |\n|     |\n|    ♣︎|\n|   10|\n  ̅̅̅̅̅'
		return f' _____\n|{self.kind}    |\n|♣︎    |\n|     |\n|    ♣︎|\n|    {self.kind}|\n  ̅̅̅̅̅'
class Diamond(Card):
	def __init__(self,kind,value):
		super().__init__(kind,value)
	def __str__(self):
		if self.kind == '10':
			return ' _____\n|10   |\n|♦︎    |\n|     |\n|    ♦︎|\n|   10|\n  ̅̅̅̅̅'
		return f' _____\n|{self.kind}    |\n|♦︎    |\n|     |\n|    ♦︎|\n|    {self.kind}|\n  ̅̅̅̅̅'
class Heart(Card):
	def __init__(self,kind,value):
		super().__init__(kind,value)
	def __str__(self):
		if self.kind == '10':
			return ' _____\n|10   |\n|♥︎    |\n|     |\n|    ♥︎|\n|   10|\n  ̅̅̅̅̅'
		return f' _____\n|{self.kind}    |\n|♥︎    |\n|     |\n|    ♥︎|\n|    {self.kind}|\n  ̅̅̅̅̅'
class Spade(Card):
	def __init__(self,kind,value):
		super().__init__(kind,value)
	def __str__(self):
		if self.kind == '10':
			return ' _____\n|10   |\n|♠︎    |\n|     |\n|    ♠︎|\n|   10|\n  ̅̅̅̅̅'
		return f' _____\n|{self.kind}    |\n|♠︎    |\n|     |\n|    ♠︎|\n|    {self.kind}|\n  ̅̅̅̅̅'

aceCl = Club('A',1)
aceDi = Diamond('A',1)
aceHt = Heart('A',1)
aceSp = Spade('A',1)
twoCl = Club('2',2)
twoDi = Diamond('2',2)
twoHt = Heart('2',2)
twoSp = Spade('2',2)
thrCl = Club('3',3)
thrDi = Diamond('3',3)
thrHt = Heart('3',3)
thrSp = Spade('3',3)
fourCl = Club('4',4)
fourDi = Diamond('4',4)
fourHt = Heart('4',4)
fourSp = Spade('4',4)
fivCl = Club('5',5)
fivDi = Diamond('5',5)
fivHt = Heart('5',5)
fivSp = Spade('5',5)
sixCl = Club('6',6)
sixDi = Diamond('6',6)
sixHt = Heart('6',6)
sixSp = Spade('6',6)
sevCl = Club('7',7)
sevDi = Diamond('7',7)
sevHt = Heart('7',7)
sevSp = Spade('7',7)
eigCl = Club('8',8)
eigDi = Diamond('8',8)
eigHt = Heart('8',8)
eigSp = Spade('8',8)
nineCl = Club('9',9)
nineDi = Diamond('9',9)
nineHt = Heart('9',9)
nineSp = Spade('9',9)
tenCl = Club('10',10)
tenDi = Diamond('10',10)
tenHt = Heart('10',10)
tenSp = Spade('10',10)
jackCl = Club('J',10)
jackDi = Diamond('J',10)
jackHt = Heart('J',10)
jackSp = Spade('J',10)
queCl = Club('Q',10)
queDi = Diamond('Q',10)
queHt = Heart('Q',10)
queSp = Spade('Q',10)
kingCl = Club('K',10)
kingDi = Diamond('K',10)
kingHt = Heart('K',10)
kingSp = Spade('K',10)

cards = [aceCl,aceDi,aceHt,aceSp,twoCl,twoDi,twoHt,twoSp,thrCl,thrDi,thrHt,thrSp,\
fourCl,fourDi,fourHt,fourSp,fivCl,fivDi,fivHt,fivSp,sixCl,sixDi,sixHt,sixSp,\
sevCl,sevDi,sevHt,sevSp,eigCl,eigDi,eigHt,eigSp,nineCl,nineDi,nineHt,nineSp,\
tenCl,tenDi,tenHt,tenSp,jackCl,jackDi,jackHt,jackSp,queCl,queDi,queHt,queSp,\
kingCl,kingDi,kingHt,kingSp]