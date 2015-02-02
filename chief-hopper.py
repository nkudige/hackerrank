# https://www.hackerrank.com/contests/w12/challenges/chief-hopper

N = int(raw_input())
h = map(int, raw_input().split())

h = [0] + h
energy = 0
energies = [energy]

for i in xrange(N):
    d = energy - h[i+1]
    energy += d
    energies.append(energy)

#print energies

print -(min(energies)/2**energies.index(min(energies)))
