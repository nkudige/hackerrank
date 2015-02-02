#https://www.hackerrank.com/contests/infinitum9/challenges/fibonacci-gcd

from math import sqrt
import decimal
decimal.getcontext().prec = 500

def fib_alt(n):
    phi = decimal.Decimal((1 + sqrt(5))/2)
    p = decimal.Decimal((1 - sqrt(5))/2)

    return int((pow(phi, n) - pow(p, n))/(phi - p))

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    x = 2

    while x < n:
        a, b = b, a+b
        x += 1

    return b

from fractions import gcd

N = int(raw_input())

g = 0
for i in xrange(N):
    if g != 1:
        g = gcd(int(raw_input()), g)

print fib_alt(g % 2000000016) % 1000000007
