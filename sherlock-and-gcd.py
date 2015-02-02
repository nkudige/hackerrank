# https://www.hackerrank.com/challenges/sherlock-and-gcd

from fractions import gcd

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().split())

    print 'NO' if reduce(gcd, A) > 1 else 'YES'
