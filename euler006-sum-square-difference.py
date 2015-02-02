# https://www.hackerrank.com/contests/projecteuler/challenges/euler006

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    print abs(sum([i**2 for i in xrange(1, N+1)]) - (N*(N+1)/2)**2)
