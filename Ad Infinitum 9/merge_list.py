#https://www.hackerrank.com/contests/infinitum9/challenges/merge-list

from math import factorial

T = int(raw_input())

for i in xrange(T):
    (N, M) = map(int, raw_input().split())

    print factorial(M+N)/(factorial(M) * factorial(N)) % 1000000007
