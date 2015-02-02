# https://www.hackerrank.com/challenges/sansa-and-xor

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    elements = [0] + map(int, raw_input().split())

    xor = 0
    for j in xrange(1, N+1):
        times = (N+1 - j) * j
#        print elements[j], times
        if not times % 2 == 0:
            xor ^= elements[j]
#            print xor
        
    print xor
