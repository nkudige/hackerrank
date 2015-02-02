# https://www.hackerrank.com/challenges/the-grid-search

T = int(raw_input())


for i in xrange(T):
    G = []
    P = []
    R, C = map(int, raw_input().split())
    for j in xrange(R):
        G.append(raw_input())

    r, c = map(int, raw_input().split())
    for j in xrange(r):
        P.append(raw_input())

    idx = -1
    for j in xrange(R):
        idx = G[j].find(P[0])
        if idx >= 0:
            x = j
            for k in xrange(1, r):
                if x < R-1:
                    x += 1
                else:
                    break
                if G[x].find(P[k]) != idx:
                    break
            else:
                print 'YES'
                break
    else:
        print 'NO'
    
