# https://www.hackerrank.com/contests/infinitum9/challenges/manasa-and-calculations

N = int(raw_input())
A = 1
B = 1

P = []
for i in xrange(N):
    (p, b, a) = map(int, raw_input().split())

    P.extend([p]*min(a,b))
    B *= p**b
    A *= p**a

s = B + A
P.sort()
for factor in P:
    B *= factor
    A /= factor
    if B <= A:
        s += (B+A)
    else:
        break

print s
