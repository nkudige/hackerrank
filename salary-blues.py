# https://www.hackerrank.com/challenges/salary-blues

from fractions import gcd

def is_all_equal(A):
    for i in xrange(len(A) - 1):
        if A[i] != A[i+1]:
            return False
    return True

(N, Q) = map(int, raw_input().split())
Z = map(int, raw_input().split())

sol = reduce(gcd, Z)
allEq = is_all_equal(Z)

for i in xrange(Q):
    K = int(raw_input())

    if sol == 1:
        A = [x + K for x in Z]
        s = reduce(gcd, A)
        print s
    elif allEq:
        print sol + K
    else:
        print sol
