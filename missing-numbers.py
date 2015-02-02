# https://www.hackerrank.com/challenges/missing-numbers

n = int(raw_input())
A = map(int, raw_input().split())

m = int(raw_input())
B = map(int, raw_input().split())

from collections import Counter

hashedA = Counter(A)
hashedB = Counter(B)

missing = []

for x in hashedB:
    if hashedB[x] - hashedA[x] > 0:
        missing.append(x)

missing.sort()

for x in missing:
    print x,
