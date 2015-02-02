#https://www.hackerrank.com/challenges/connecting-towns

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    ni = map(int, raw_input().split())

    product = 1

    for routes in ni:
        product *= routes
        product %= 1234567

    print product
