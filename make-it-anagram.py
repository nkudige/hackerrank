# https://www.hackerrank.com/challenges/make-it-anagram

from collections import Counter

s1 = raw_input()
s2 = raw_input()

hash1 = Counter(s1)
hash2 = Counter(s2)

toDelete = 0
checked = []

for [key, value] in hash1.iteritems():
    toDelete += abs(value - hash2.get(key, 0))
    checked.append(key)

for [key, value] in hash2.iteritems():
    if key not in checked:
        toDelete += value

print toDelete
