# https://www.hackerrank.com/challenges/game-of-rotation

N = int(raw_input())
list = [0] + map(int, raw_input().split())

s = 0
values = [0]*(N+1)

for i in xrange(1, N+1):
    s += list[i]
    values[i] = i*list[i]

PMEAN = sum(values)
#print PMEAN
maxPMEAN = PMEAN

for i in xrange(1, N+1):
    PMEAN = PMEAN - s + N*list[i]
    maxPMEAN = PMEAN if PMEAN > maxPMEAN else maxPMEAN
#    print newPMEAN

print maxPMEAN
