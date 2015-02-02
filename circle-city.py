# https://www.hackerrank.com/challenges/circle-city

from math import sqrt
from math import floor
from math import ceil

t = int(raw_input())

for i in xrange(t):
    (r, k) = map(int, raw_input().split())

    Nr = 1 + 4*int(floor(sqrt(r)))

    t = 0
    for j in xrange(1, int(floor(sqrt(r)))):
        t += int(floor(sqrt(r - j**2)))

    Nr += 4*t
    Lr = 8*Nr - 4

    print Lr
        
