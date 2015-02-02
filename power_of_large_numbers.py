# https://www.hackerrank.com/challenges/power-of-large-numbers

T = int(raw_input())

for i in xrange(T):
    (A, B) = map(int, raw_input().split())
    print int(pow(A, B, 1000000007)) % 1000000007
