# https://www.hackerrank.com/challenges/handshake

from math import factorial

##f = [1]

##def factorial(N):
##    global f
##    if len(f) > N:
##        return f[N]
##    f.append(N * factorial(N-1))
##    return f[N]

def combinations(N):
    if N < 2:
        return 0
    fn2 = factorial(N-2)
    return fn2*(N-1)*N / (2*fn2)

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())

    print combinations(N)
