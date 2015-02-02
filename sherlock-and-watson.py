# https://www.hackerrank.com/challenges/sherlock-and-watson

N, K, Q = map(int, raw_input().split())

A = map(int, raw_input().split())

for i in xrange(Q):
    x = int(raw_input())
    print A[(x + N - (K%N))%N]
