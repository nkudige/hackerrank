# https://www.hackerrank.com/challenges/count-luck

def wave_magic(forest, i, j, N, M, k):
    global visited, kright

#    print i, j, k
    if forest[i][j] == '*':
        kright = k
#        print 'BINGO!'
        return k

    if visited[i][j]:
#        print 'wut'
        return 0
    
    visited[i][j] = True

    allVisited = True
    for ab in xrange(N+1):
        for cd in xrange(M+1):
            if not visited[ab][cd]:
                allVisited = False
                break

    if allVisited:
#        print 'wut'
        return 0
    
    
    c = 0
    c += 1 if i < N and (forest[i+1][j] == '.' or forest[i+1][j] == '*') and not visited[i+1][j] else 0
    c += 1 if j < M and (forest[i][j+1] == '.' or forest[i][j+1] == '*') and not visited[i][j+1] else 0
    c += 1 if i > 0 and (forest[i-1][j] == '.' or forest[i-1][j] == '*') and not visited[i-1][j] else 0
    c += 1 if j > 0 and (forest[i][j-1] == '.' or forest[i][j-1] == '*') and not visited[i][j-1] else 0

    if c >= 2:
        k = k + 1

    p, q, r, s = 0, 0, 0, 0
#    print visited
    if i < N and (forest[i+1][j] == '.' or forest[i+1][j] == '*') and not visited[i+1][j]:
        p = wave_magic(forest, i+1, j, N, M, k)

    if i > 0 and (forest[i-1][j] == '.' or forest[i-1][j] == '*') and not visited[i-1][j]:
        q = wave_magic(forest, i-1, j, N, M, k)

    if j < M and (forest[i][j+1] == '.' or forest[i][j+1] == '*') and not visited[i][j+1]:
        r = wave_magic(forest, i, j+1, N, M, k)

    if j > 0 and (forest[i][j-1] == '.' or forest[i][j-1] == '*') and not visited[i][j-1]:
        s = wave_magic(forest, i, j-1, N, M, k)
        
    return max(p, q, r, s)
        
    
def get_position(forest, ch):
    return next(((i, row.index(ch))
                   for i, row in enumerate(forest)
                   if ch in row),
                  None)

T = int(raw_input())

for i in xrange(T):
    [N, M] = map(int, raw_input().split())

    forest = []

    for j in xrange(N):
        forest.append(list(raw_input()))

    K = int(raw_input())

    (x, y) = get_position(forest, 'M')
    #print m, n
    #print x, y

    visited = [[False]*M for j in xrange(N)]
    for m in xrange(N):
        for n in xrange(M):
            if forest[m][n] == 'X':
                visited[m][n] = True

    kright = -1
    k = wave_magic(forest, x, y, N-1, M-1, 0)
#    print k
#    print visited
    print "Impressed" if k == K else "Oops!"
