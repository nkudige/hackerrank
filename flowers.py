#https://www.hackerrank.com/challenges/flowers

[N, K] = map(int, raw_input().split())
costs =  map(int, raw_input().split())
costs.sort()
costs.reverse()

total = sum(costs[:K])
if K < N:
    i = 1
    j = 0
    for cost in costs[K:]:
        total += (i+1)*cost
        j += 1
        if j % K == 0:
            i += 1

print total
