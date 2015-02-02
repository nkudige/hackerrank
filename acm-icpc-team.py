# https://www.hackerrank.com/challenges/acm-icpc-team

def setBitCount(n):
    c = 0
    while n >= 1:
        c += 1 if n % 2 == 1 else 0
        n >>= 1
    return c

(N, M) = map(int, raw_input().split())
p = []

for i in xrange(N):
    p.append(int(raw_input(), 2))

m = 0
mC = 0

for i in xrange(N):
    for j in xrange(i+1, N):
        o = p[i] | p[j]
        mC = mC+1 if o == m else 1 if o > m else mC
        m = o if o > m else m
#        print mC

print setBitCount(m)
print mC
