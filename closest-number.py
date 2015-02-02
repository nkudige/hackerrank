# https://www.hackerrank.com/challenges/closest-number

T = int(raw_input())

for i in xrange(T):
    (a, b, x) = map(int, raw_input().split())
    target = a**b
    divisor = int(target / x)
    print x*divisor if abs(x*divisor - target) <= abs(x*(divisor+1) - target) else x*(divisor+1)
