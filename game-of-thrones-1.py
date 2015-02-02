#https://www.hackerrank.com/challenges/game-of-thrones

from collections import Counter
from math import factorial

s = raw_input()

hashed = Counter(s)

odds = 0
evens = 0
vals = []

for value in hashed.values():
    if value % 2 != 0:
        odds += 1
    else:
        vals.append(value/2)
        
    if odds > 1:
        print 'NO'
        break
    
else:
    print 'YES'
