# https://www.hackerrank.com/challenges/icecream-parlor

T = int(raw_input())

for i in xrange(T):
    M = int(raw_input())
    N = int(raw_input())
    costs = map(int, raw_input().split())

    c = [y for y in costs]
    c.sort()

    result = []
    m, n = 0, 0

    for j in xrange(N):
        s = c[j]
        for k in xrange(N-1, j, -1):
            if s + c[k] == M:
                result.extend([s, c[k]])
                break
            elif s + c[k] < M:
                break
        if len(result) > 0:
            break

    for j in xrange(N):
        if result[0] == costs[j] and m == 0:
            m = j+1

        if result[1] == costs[j] and m != j+1:
            n = j+1
            
    if m < n:
        print m, n
    else:
        print n, m
