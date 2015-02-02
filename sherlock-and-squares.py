# https://www.hackerrank.com/challenges/sherlock-and-squares

from math import sqrt
from math import ceil
from math import floor

T = int(raw_input())

for i in xrange(T):
    (A, B) = map(int, raw_input().split())

    c = 0
    for i in xrange(int(ceil(sqrt(A))), int(floor(sqrt(B))+1)):
        c += 1

    print c
