# https://www.hackerrank.com/challenges/easy-sum

def summation(n):
    return n*(n+1)/2

def easy_sum(n, m):
    t = n / m
    s = summation(m-1) * t
    s += summation(n % m)
    return s

T = int(raw_input())

for i in xrange(T):
    (N, m) = map(int, raw_input().split())
    print easy_sum(N, m)
