# https://www.hackerrank.com/contests/projecteuler/challenges/euler005
from fractions import gcd
def lcm(a, b):
    return a * b / gcd(a, b)

T = int(raw_input())
for i in xrange(T):
    print reduce(lcm, range(1, int(raw_input())+1))
