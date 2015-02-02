T = int(raw_input())

for i in xrange(T):
    p = []
    for j in xrange(4):
        p.append(map(int, raw_input().split()))

    c = 0
    for j in xrange(3):
        for k in xrange(3):
            if p[k][j] != p[k+1][j]:
                break
        else:
            c += 1
            break

    print 'YES' if c > 0 else 'NO'
