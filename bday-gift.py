# https://www.hackerrank.com/challenges/bday-gift

N = int(raw_input())

p = 0.0

for i in xrange(N):
    p += int(raw_input())/2.0

print p
