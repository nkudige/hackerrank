# https://www.hackerrank.com/challenges/filling-jars

(N, M) = map(int, raw_input().split())

total = 0
for i in xrange(M):
    (a, b, k) = map(int, raw_input().split())
    total += (b+1 - a) * k

print total / N
