# https://www.hackerrank.com/challenges/triangle-numbers

def generate_triangle(N):
    a = [1, 4, 10, 16, 19]
    n = 5

    if N <= 5:
        if N == 1 or N == 2:
            return -1
        elif N == 3 or N == 5:
            return 2
        elif N == 4:
            return 3
    
    for i in xrange(5, N+1):
        b = []
        for j in xrange(5):
            end = j+1 if j+1 < len(b) else len(b)
            start = 0 if end - 2 < 0 else end - 2
            x = sum(a[start:end+1])
            b.append(x)
        a = b

    #print a
    for i, val in enumerate(a):
        if val % 2 == 0:
            return i+1

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    print generate_triangle(N)
