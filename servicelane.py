# https://www.hackerrank.com/challenges/service-lane

[N, T] = map(int,raw_input().split())

width = map(int, raw_input().split())

def smallest(width, i, j):
    small = 4
    for x in xrange(i, j+1):
        if width[x] < small:
            small = width[x]
        if small == 1:
            return small
    return small

for i in xrange(T):
    [i, j] = map(int, raw_input().split())
    print smallest(width, i, j)
