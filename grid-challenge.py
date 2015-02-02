# https://www.hackerrank.com/contests/101hack18/challenges/grid-challenge

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())

    G = []
    for j in xrange(N):
        G.append(sorted(list(raw_input())))

    flag = True
    for j in xrange(N):
        for k in xrange(N-1):
            if G[k][j] > G[k+1][j]:
                flag = False
                break
        if not flag:
            break

    print 'YES' if flag else 'NO'
            
    
