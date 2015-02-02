# https://www.hackerrank.com/contests/infinitum9/challenges/demidenko-computer-virus

Q = int(raw_input())

for i in xrange(Q):
    (n, t) = map(int, raw_input().split())

    infected = 1
    
    for j in xrange(1, t+1):
        infected += (2**j)*n

    print infected
