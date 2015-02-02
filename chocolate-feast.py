#https://www.hackerrank.com/challenges/chocolate-feast

T = int(raw_input())

for i in xrange(T):
    (N, C, M) = map(int, raw_input().split())

    c = N / C

    totalC = c

    while True:
        c -= M
        if c < 0:
            break
        totalC += 1
        c += 1

    print totalC
