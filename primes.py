from math import sqrt

N = 200000
c = 1

primes = [2]

for X in xrange(3, N, 2):
    for i in xrange(3, int(sqrt(X))+1):
        if X % i == 0:
            break
    else:
        primes.append(X)
        c += 1

print primes
print c
