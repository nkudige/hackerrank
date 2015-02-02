# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

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

print isPrime(707)
