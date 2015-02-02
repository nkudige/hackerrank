# https://www.hackerrank.com/contests/w12/challenges/chief-hopper

N = int(raw_input())
h = map(int, raw_input().split())

h = [0] + h
energy = 0
minEnergy = 1000001
minEnergyIdx = -1

for i in xrange(N):
    d = energy - h[i+1]
    energy += d
    if energy < minEnergy:
        minEnergy = energy
        minEnergyIdx = i+1

#print energies

print -(minEnergy/2**minEnergyIdx)
