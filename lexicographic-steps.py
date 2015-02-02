# https://www.hackerrank.com/challenges/lexicographic-steps

from itertools import permutations
from collections import Counter

def set_bits(rInt):
    v = rInt
    c = 0
    while v > 0:
        v &= (v-1)
        c += 1
    return c

T = int(raw_input())

for i in xrange(T):
    (x, y, K) = map(int, raw_input().split())
    
    result = "0"*x + "1"*y
#    print result
    rInt = int(result, 2)
    k = 0
    
    while True:
        rInt += 1

        setBits = set_bits(rInt)
        k += 1 if setBits == y else 0
#        rBin = bin(rInt)[2:]
#        rBin = '0'*(len(result) - len(rBin)) + rBin
#        print rBin, k
#        raw_input()
#        print rBin
#        k += 1 if Counter(rBin)['0'] == x else 0
        if k == K:
#            print rBin
            break

    rBin = bin(rInt)[2:]
    rBin = "0" * (len(result) - len(rBin)) + rBin
    minato = "" 
    for char in rBin:
        minato += 'H' if char == '0' else 'V'

    print minato
