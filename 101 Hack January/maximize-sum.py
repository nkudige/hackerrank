T = int(raw_input())

for t in xrange(T):
    N, M = map(int, raw_input().split())
    a = map(int, raw_input().split())

    max = 0

    flag = False
    for j in xrange(N):
        s = 0
        for i in xrange(j, N):
            s = (s + a[i]) % M
            max = s if s > max else max
            if max == M - 1:
                flag = True
                break
        if flag:
            break
    print max
