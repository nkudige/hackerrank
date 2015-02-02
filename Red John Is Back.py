# https://www.hackerrank.com/challenges/red-john-is-back

from math import factorial
from math import sqrt

def countPrimes(N):
    if N < 2:
        return 0
    if N == 2:
        return 1
    
    c = 1
    
    for X in xrange(3, N+1, 2):
        for i in xrange(3, int(sqrt(X))+1):
            if X % i == 0:
                break
        else:
            c += 1

    return c

T = int(raw_input())

def differentWays(N):
    if N == 0:
        return 1
    return differentWays(N-1) + differentWays(N-4) if N >= 4 else differentWays(N-1)
    

for i in xrange(T):
    N = int(raw_input())


    print countPrimes(differentWays(N))
