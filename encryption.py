# https://www.hackerrank.com/challenges/encryption

from math import sqrt
from math import floor
from math import ceil

s = raw_input()
s = s.replace(" ", "")

l = len(s)

r = c = int(floor(sqrt(l)))

c += 1 if r*c < l else 0
r += 1 if r*c < l else 0

#print r,c
result = ""

for i in xrange(c):
    j = 0
    while i+j < l:
        result += s[i+j]
        j += c
    result += " "

print result
