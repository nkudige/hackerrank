from bisect import bisect_left
from math import ceil
from math import floor
from math import sqrt

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos

N = int(raw_input())
R = sorted(map(int, raw_input().split()))
M = int(raw_input())

x = {}

count = 0
for i in xrange(M):
    (x1, y1, x2, y2) = map(int, list(raw_input().split()))

    t1 = pow(x1, 2) + pow(y1, 2)
    t2 = pow(x2, 2) + pow(y2, 2)

    lower = int(ceil(sqrt(t1)))
    upper = int(ceil(sqrt(t2)))

    if upper < lower:
        lower, upper = upper, lower

    print binary_search(R, upper, 0, N), binary_search(R, lower, 0, N)
    
    count += ( binary_search(R, upper, 0, N) - binary_search(R, lower, 0, N))
    
    
    
##    
##    for j in range(N):
##        count += 1 if (t1 < R[j] and t2 > R[j]) or (t1 > R[j] and t2 < R[j]) else 0
##
##count = 0
##for i in xrange(N):
##    count += x.get(R[i], 0)
##
##
print count
