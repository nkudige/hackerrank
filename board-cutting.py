# https://www.hackerrank.com/challenges/board-cutting

T = int(raw_input())

for i in xrange(T):
    (M, N) = map(int, raw_input().split())

    y = sorted(map(int, raw_input().split()), reverse=True)
    x = sorted(map(int, raw_input().split()), reverse=True)

    H = V = 1

    Ml = M - 1
    Nl = N - 1

    cost = 0
    
    while True:
#        print y, Ml
#        print x, Nl
        
        if Nl == 0 or (Ml > 0 and (y[0] > x[0] or (y[0] == x[0] and Ml > Nl))):
            cost += y[0]*V
            H += 1
            y.remove(y[0])
            Ml -= 1
            
        elif Nl > 0:
            cost += x[0]*H
            V += 1
            x.remove(x[0])
            Nl -= 1

        if Ml == 0 and Nl == 0:
            break

    print cost % 1000000007
