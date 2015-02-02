# https://www.hackerrank.com/challenges/sherlock-and-queries

from operator import mul

N, M = map(int, raw_input().split())

A = [0] + map(int, raw_input().split())
B = [0] + map(int, raw_input().split())
C = [0] + map(int, raw_input().split())


##for i in xrange(1, M+1):
##    for j in xrange(1, N+1):
##        if j % B[i] == 0:
##            A[j] *= C[i]
##            A[j] %= 1000000007
##            print j, i, A[j], C[i]
##
##for i in xrange(1, N+1):
##    print A[i],


jmb = {}

for i in xrange(1, M+1):
    t = 0
    x = B[i]
    while True:
        t += x
        if t > N:
            break
#        print i, t
#        raw_input()
        jmb[t] = jmb.get(t, [])
        jmb[t].append(C[i])

#print jmb

for i in xrange(1, N+1):
    A[i] = A[i] * reduce(mul, jmb[i], 1) % 1000000007
    
for i in xrange(1, N+1):
    print A[i],
