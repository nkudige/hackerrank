#https://www.hackerrank.com/challenges/find-digits

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    n = map(int, list(str(N)))

    c = 0
    for num in n:
        if num == 0:
            continue
        c += 1 if N % num == 0 else 0

    print c
