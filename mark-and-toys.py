# https://www.hackerrank.com/challenges/mark-and-toys

N, K = map(int, raw_input().split())
prices = map(int, raw_input().split())

prices.sort()
cost = 0
count = 0

#print prices

while count < N:
 #   print cost, count
    if cost + prices[count] > K:
        break
    cost += prices[count]
    count += 1

print count
