# https://www.hackerrank.com/challenges/journey-to-the-moon
from math import factorial

def combinations(n, r):
    if n < r:
        return 0
    return factorial(n)/(r*factorial(n-r))

astronauts = []

[N, I] = map(int, raw_input().split())

for i in xrange(I):
    pair = map(int, raw_input().split())

    n = len(astronauts)
    
    for j in xrange(n):
        if pair[0] in astronauts[j] or pair[1] in astronauts[j]:
            astronauts[j].add(pair[0])
            astronauts[j].add(pair[1])
            break
    else:
        astronauts.append(set())
        astronauts[n].add(pair[0])
        astronauts[n].add(pair[1])


#print astronauts

for i in xrange(len(astronauts)-1):
    for j in xrange(i+1, len(astronauts)):
        if len(astronauts[i].intersection(astronauts[j])) > 0:
            astronauts[i] = astronauts[i].union(astronauts[j])
            astronauts[j] = set()


sooper = 0
astro = [i for i in xrange(N)]
res = set(astro) - set().union(*astronauts)
if len(res) > 0:
    sooper = len(res)

product = 0
for i in xrange(len(astronauts)):
    for j in xrange(i+1, len(astronauts)):
        product += (len(astronauts[i]) * len(astronauts[j]))
    product += (len(astronauts[i]) * sooper)

product += combinations(sooper, 2)

#print astronauts
print product
