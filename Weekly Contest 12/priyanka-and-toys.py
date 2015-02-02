# https://www.hackerrank.com/contests/w12/challenges/priyanka-and-toys

N = int(raw_input())
cost = map(int, raw_input().split())

cost.sort()

amount = 0

rangeBegin = 0

for i in xrange(1, N):
    if i == N-1:
        amount += 1
        
    if cost[i] - cost[rangeBegin] <= 4:
        continue

    rangeBegin = i
    amount += 1

print amount
