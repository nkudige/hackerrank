#https://www.hackerrank.com/challenges/lonely-integer

N = int(raw_input())
A = map(int, raw_input().split())

n = [0] * 101

for i in xrange(len(A)):
    n[A[i]] += 1

for i in xrange(101):
    if n[i] == 1:
        print i
