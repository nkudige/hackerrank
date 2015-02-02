# https://www.hackerrank.com/challenges/sherlock-and-pairs

from math import factorial

def combinations(n, r):
    if n == 1:
        return 0

    x = factorials.get(n, -1)
    if x == -1:
        x = factorial(n-r)
        factorials[n-r] = x
        factorials[n] = x*(n-1)*n
        
    return x*(n-1)*n / x

T = int(raw_input())
factorials = {}

for i in xrange(T):
    N = int(raw_input())
    l = map(int, raw_input().split())
    
    l.sort()
    l.append(0)

    eq = 1
    result = 0
    for j in xrange(1, N+1):
        if l[j] == l[j-1]:
            eq += 1
            continue

        result += combinations(eq, 2)
        eq = 1
    print result

##print combinations(4, 2)
