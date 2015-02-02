from math import sqrt

def count_pairs(D, P):
    c = 0
    d = int(pow(D,2)) - 4*(-P)
    if d == 0:
        c += 1 if -D/2.0 == int(-D/2.0) else 0
        c += 1 if D/2.0 == int(D/2.0) and (D/2.0) != (-D/2.0) else 0
#        print D/2.0, -D/2.0
    elif d > 0:
        c += 1 if (-D + sqrt(d))/2.0 == int((-D + sqrt(d))/2.0) else 0
        c += 1 if (-D - sqrt(d))/2.0 == int((-D - sqrt(d))/2.0) else 0
        c += 1 if (D + sqrt(d))/2.0 == int((D + sqrt(d))/2.0) and ((-D + sqrt(d))/2.0) != (D + sqrt(d))/2.0 else 0
        c += 1 if (D - sqrt(d))/2.0 == int((D - sqrt(d))/2.0) and ((D - sqrt(d))/2.0) != ((-D - sqrt(d))/2.0) else 0

        print (-D + sqrt(d))/2.0, (-D - sqrt(d))/2.0, (D + sqrt(d))/2.0, (D - sqrt(d))/2.0
        
    return c

T = int(raw_input())

for i in xrange(T):
    (D, P) = map(int, raw_input().split())

    if D < 0:
        print 0
    else:
        print count_pairs(D, P)
