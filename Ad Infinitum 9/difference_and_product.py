#https://www.hackerrank.com/contests/infinitum9/challenges/difference-and-product

def factors(n):
    if n == 0:
        return [[0,0]]
    return list(reduce(list.__add__, 
                ([[-i, -n/i], [i, n//i]] for i in range(1, int(abs(n)**0.5) + 1) if abs(n) % i == 0)))

T = int(raw_input())

for i in xrange(T):
    (D, P) = map(int, raw_input().split())

    if D < 0:
        print 0
        continue
    
    s = factors(P)
    print s
    c = 0

    for pair in s:
        c += 1 if abs(pair[0] - pair[1]) == D else 0
        c += 1 if pair[0] != pair[1] and abs(pair[1] - pair[0]) == D else 0

    print c
