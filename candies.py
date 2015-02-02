# https://www.hackerrank.com/challenges/candies

def candies_to_buy(n):
    global s, rating

    if s[n] != -1:
        return s[n]

    x = candies_to_buy(n-1) if rating[n] > rating[n-1] else 0
    y = candies_to_buy(n+1) if rating[n] > rating[n+1] else 0

    result = max(x, y) + 1
    return result

N = int(raw_input())
rating = [100001]

for i in xrange(N):
    rating.append(int(raw_input()))

rating.append(100001)

s = [-1]*(N+2)

for i in xrange(1, N+1):
    s[i] = candies_to_buy(i)

s = s[1:-1]
#print s
print sum(s)
