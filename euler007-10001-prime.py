# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

from math import sqrt

primes = [2]

def generate_primes():
    global primes
    c, i = 1, 3
    while c < 10001:
        for j in xrange(3, int(sqrt(i))+1, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
            c += 1
        i += 2

T = int(raw_input())
generate_primes()

for i in xrange(T):
    N = int(raw_input())
    print primes[N-1]
