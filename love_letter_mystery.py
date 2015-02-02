# https://www.hackerrank.com/challenges/the-love-letter-mystery

T = int(raw_input())

def changes(s):
    i = 0
    n = len(s) - 1
    c = 0
    while i < n:
        
        if s[i] != s[n]:
            c += abs(ord(s[n]) - ord(s[i]))

        i += 1
        n -= 1

    return c


for i in xrange(T):
    s = raw_input()

    print changes(s)
