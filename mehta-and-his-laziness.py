# https://www.hackerrank.com/challenges/mehta-and-his-laziness

from math import sqrt
from fractions import gcd

def get_simplified_pq(p, q):
    g = gcd(p, q)
    return (p/g, q/g)

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    f = factors(N)

    evensquares = [x for x in f if x % 2 == 0 and int(sqrt(x))**2 == x and x != N]

    p = len(evensquares)
    q = len(f)

    (p, q) = get_simplified_pq(p, q-1)
    
    print "0" if p == 0 else "%d/%d" % (p, q)
