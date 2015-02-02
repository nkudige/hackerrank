# https://www.hackerrank.com/challenges/summing-the-n-series

T = int(raw_input())
for i in xrange(T):
    n = int(raw_input())
    print n**2 % 1000000007
