#https://www.hackerrank.com/contests/infinitum9/challenges/eulers-criterion

T = int(raw_input())

for i in xrange(T):
    (A, M) = map(int,raw_input().split())
    print 'NO' if pow(A, (M-1)/2, M) > 1 else 'YES'
