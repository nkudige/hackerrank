def onTime(t, N, K):
    c = 0
    for i in xrange(N):
        c += 1 if t[i] <= 0 else 0
        if c >= K:
            return 'NO'

    return 'YES'
            

T = int(raw_input())

for i in xrange(T):
    N, K = map(int, raw_input().split())
    t = map(int, raw_input().split())

    print onTime(t, N, K)
