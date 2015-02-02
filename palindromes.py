# https://www.hackerrank.com/challenges/palindromes

from collections import Counter
from math import factorial

def is_palindrome(s):
    n = len(s) - 1
    i = 0
    while i < n:
        if s[i] != s[n]:
            return False
        i += 1
        n -= 1
    return True

def palindrome_anagram_count(s):
    hashed = Counter(s)

    odds = 0
    evens = 0
    vals = []

    for value in hashed.values():
        if value % 2 != 0:
            odds += 1
            if value / 2 >= 1:
                vals.append(value/2)
        else:
            vals.append(value/2)
            
        if odds > 1:
            return 0
        
    else:
            sol = factorial(sum(vals))
##            for val in vals:
##                if val > 1:
##                    sol /= factorial(val)
                    
            return sol


T = int(raw_input())

for i in xrange(T):
    s = raw_input()

    n = palindrome_anagram_count(s)

    slen = len(s)

    if slen < 2 or is_palindrome(s):
        print '0.0000'

    else:
        t = factorial(slen-2)
        c = t * (slen-1) * slen / (2 * t)

        print c, n
        result = float(c) / n
        print '%.4f' % result
