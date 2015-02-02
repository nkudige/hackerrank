T = int(raw_input())

for i in xrange(T):
    B, W = map(int, raw_input().split())
    X, Y, Z = map(int, raw_input().split())

    a = B * X + W * Y
    b = B * X + W * (X+Z)
    c = B * (Y+Z) + W * Y
    
    print min(a, b, c)
