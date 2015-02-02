#https://www.hackerrank.com/contests/101hack20/challenges/and-product

T = int(raw_input())

for i in xrange(T):
    (A, B) = map(int, raw_input().split())

    res = A
    for j in xrange(A+1, B+1):
        res &= j

    print res
 
