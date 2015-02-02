# https://www.hackerrank.com/challenges/john-and-gcd-list

from fractions import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    A = map(int, raw_input().split())

    B = [A[0]]

    for j in xrange(1, N):
        B.append(lcm(A[j-1], A[j]))

    B.append(A[N-1])

    for x in B:
        print x,
    print
