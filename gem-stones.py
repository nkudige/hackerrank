# https://www.hackerrank.com/challenges/gem-stones

N = int(raw_input())

stones = [0] * 26
gems = 0

for i in xrange(N):
    s = raw_input()
    n = len(s)
    flags = [False]*26
    
    for j in xrange(n):
        idx = ord(s[j]) - 97
        if not flags[idx]:
            stones[idx] += 1
            flags[idx] = True

            if stones[idx] == N:
                gems += 1

print gems
