# https://www.hackerrank.com/challenges/even-odd-query

def find(x, y):
    global A
    print x, A[x-1], y
    raw_input()
    if x == 0:
        return 0
    if x > y or x >= len(A):
        return 1
    return 1*find(x+1, y)

N = int(raw_input())
A = map(int, raw_input().split())

Q = int(raw_input())
for i in xrange(Q):
    (a, b) = map(int, raw_input().split())
    print 'Even' if A[a-1] % 2 == 0 and find(a, b) != 0 else 'Odd'
