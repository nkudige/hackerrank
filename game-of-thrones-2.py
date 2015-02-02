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
        if value / 2 >= 1:
            vals.append(value/2)
    else:
        vals.append(value/2)
        
    if odds > 1:
        print 0
        break
    
else:
        sol = factorial(sum(vals))
        for val in vals:
            if val > 1:
                sol /= factorial(val)
                
        print sol%1000000007
