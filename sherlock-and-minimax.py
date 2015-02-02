# https://www.hackerrank.com/challenges/sherlock-and-minimax

from math import ceil

N = int(raw_input())
A = map(int, raw_input().split())
(P, Q) = map(int, raw_input().split())

R = int(ceil((Q + P) / 2.0))

minP = min([abs(A[i] - P) for i in xrange(N)])
minR = min([abs(A[i] - R) for i in xrange(N)])
minQ = min([abs(A[i] - Q) for i in xrange(N)])

sol = R if minR >= minQ else Q
m = minR if sol == R else minQ

sol = P if minP >= m else sol

print sol
