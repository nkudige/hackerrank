#https://www.hackerrank.com/challenges/sherlock-and-divisors

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    f = factors(N)
    c = 0
    for val in f:
        c += 1 if val % 2 == 0 else 0
    print c
