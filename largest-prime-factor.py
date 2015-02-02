# https://www.hackerrank.com/contests/projecteuler/challenges/euler003

from math import sqrt

def isPrime(n):
    if n <= 1:
        return false
    if n == 2:
        return True

    for i in xrange(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False

    return True

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

T = int(raw_input())

for i in xrange(T):
    N =int(raw_input())

    f = factors(N)
    oddfactors = [x for x in f if x % 2 == 1]

    for v in sorted(oddfactors, reverse=True):
        if isPrime(v):
            print v
            break
