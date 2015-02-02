# https://www.hackerrank.com/challenges/die-hard-3

def is_possible(a, b, c):
    possible = [a, b]
    if c in possible:
        return True
    while b > 0:
        a = a - b
        possible.append(a)
        (a, b) = (b, a) if a < b else (a, b)

    a = set(x + y for x in possible for y in possible)
    a = sorted(a)
    
    return True if c in a else False

T = int(raw_input())

for i in xrange(T):
    (a, b, c) = map(int, raw_input().split())
    (a, b) = (b, a) if a < b else (a, b)
    
    print 'YES' if is_possible(a, b, c) else 'NO'
