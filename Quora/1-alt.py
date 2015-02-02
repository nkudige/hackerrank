from math import sqrt

c = 0

N = int(raw_input())
R = map(int, raw_input().split())

M = int(raw_input())
points = []
for i in xrange(M):
    #points.append(tuple(map(int, raw_input().split())))
    (x1, y1, x2, y2) = (tuple(map(int, raw_input().split())))

    for j in xrange(N):
        A = int(pow(x1, 2)) - 2*x1*x2 + int(pow(x2, 2)) + int(pow(y1, 2)) - 2*y1*y2 + int(pow(y2, 2))
        B = 2*x1*x2 - 2*int(pow(x2, 2)) + 2*y1*y2 - 2*int(pow(y2, 2))
        C = int(pow(x2, 2)) + int(pow(y2, 2)) - int(pow(R[j], 2))

        d = int(pow(B, 2))-4*A*C

        g = 0
        if d >= 0:
            t = (float(-B) + sqrt(d)) / (2*A)
#            print t
            g += 1 if t >= 0 and t <= 1 else 0
            t = (float(-B) - sqrt(d)) / (2*A)
            g += 1 if t >= 0 and t <= 1 else 0

#            print t
        
        c += 1 if g == 1 else 0

print c
