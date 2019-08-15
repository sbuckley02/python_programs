'''
Story Time
It was nearing Christmas. My friend suggested that we do Secret Santa this year, where everyone
has a person to give a gift to, but no one knows who everyone else has. I agreed.

How were we supposed to accomplish this? All eight of us could not gather in the same place
at the same time before when we wanted to exchange gifts. While waiting to run at a track
meet, I had a solution.

I created this, a program which randomly assigns everyone another for Secret Santa. No one gets
themselves, and no one gets someone who has already been assigned.

There was one issue I had to deal with: I can't tell people who they have without spoiling the
entire game for myself. After all, I want to play too. Thus, I had the program convert who
everyone has into binary. I cannot in my right mind decipher what letter 1001101 is. I can,
however, have an idea of who has who based on the amount of letters. I then had to make it so
that each name had 6 characters. I added random characters to people's names to do this.

So, how did people know who they have with just these binary digits? Let me take you through the
process:
The output of the program gives lines like these:
Andrew has 1001101 1100001 1100100 1100100 1101001 1100101
Maddie has 1001100 1110101 1100011 1111001 1011011 1011101
I would then send Andrew and Maddie those exact codes. I would then tell them to visit this
website: https://www.rapidtables.com/convert/number/binary-to-ascii.html
On this website, they could copy and paste the binary code to find who they had.
Andrew would find out that he had Maddie, while Maddie would find out that she had Lucy.

When I used this, it worked completely.
'''

from random import randint
from bin import text_to_bin

names = ['Andrew','Maddie','Steve%','Reese@','Jonas>','Josh()','Lucy[]','Mike><']
tracker = [[0,None],[1,None],[2,None],[3,None],[4,None],[5,None],[6,None],[7,None]]
avail = [0,1,2,3,4,5,6,7]

def test():
    result = 'pass'
    for p1,p2 in tracker:
        if p1 == p2:
            result = 'fail'
            break
    return result

for index,item in enumerate(tracker):
    rand = randint(0,7)
    while rand not in avail:
        rand = randint(0,7)
    avail.remove(rand)
    tracker[index][1] = rand

while True:
    rand1 = randint(0,7)
    rand2 = randint(0,7)
    storage = tracker[rand1][1]
    tracker[rand1][1] = tracker[rand2][1]
    tracker[rand2][1] = storage
    if test() == 'pass':
        break

for num in range(8):
    print(f'{names[num]} has {text_to_bin(names[tracker[num][1]])}')
