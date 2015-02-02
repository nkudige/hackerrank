from collections import Counter

N = int(raw_input())
cost = map(int, raw_input().split())

m = min(cost)

cost = [(x-(m%5))/4 for x in cost]

hashed = Counter(cost)

print len(hashed)
