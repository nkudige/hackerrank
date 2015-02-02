# https://www.hackerrank.com/contests/pythonista-practice-session/challenges/sets

M = int(raw_input())
m = map(int, raw_input().split())

N = int(raw_input())
n = map(int, raw_input().split())

set_m = set(m)
set_n = set(n)

res = list(set_m - set_n)
res.extend(list(set_n - set_m))

res.sort()

for val in res:
    print val
