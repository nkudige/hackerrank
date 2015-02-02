# https://www.hackerrank.com/challenges/mr-k-marsh

(m, n) = map(int, raw_input().split())

land = []
for i in xrange(m):
    land.append(map(str,list(raw_input().split())))

top = left = 0
bottom = m-1
right = n-1

while True:
    if isGoodRow(
