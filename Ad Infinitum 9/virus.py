#https://www.hackerrank.com/contests/infinitum9/challenges/demidenko-computer-virus

Q = int(raw_input())

for i in xrange(Q):
    (n, t) = map(int, raw_input().split())

    if t == 0:
        print 1
    else:
        a = n
        
        res = n * (2**(t) - 1)/(2 - 1)
        print res
