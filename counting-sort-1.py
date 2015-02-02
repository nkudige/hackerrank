# https://www.hackerrank.com/challenges/countingsort1

from collections import Counter

raw_input()
hashed = Counter(map(int, raw_input().split()))

for i in xrange(100):
    print hashed.get(i, 0),
