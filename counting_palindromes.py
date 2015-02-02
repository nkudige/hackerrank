# https://www.hackerrank.com/challenges/count-palindromes

import math

T = int(raw_input())

finasol = []

def try_all_combos(sol, K):
    global finalsol
    n = get_palindrome_count(sol)
#    print sol,n
    if n == K:
        finalsol = [sol, n]
        return True
    elif n > K:
        return False
    elif n < K:
        flag = False
        for i in xrange(97, 123):
            flag = try_all_combos(sol+chr(i), K)
            if flag:
                break
        else:
            return False

        return True
            

def get_palindrome_count(sol):
    c = 0
    for s in get_all_substrings(sol):
        c += 1 if isPalindrome(s) else 0
    return c

def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

def isPalindrome(string):
    n = len(string)-1
    i = 0
    while i < n:
        if string[i] != string[n]:
#            print 'Not Palindrome: ', string
            return False
        i += 1
        n -= 1
#    print 'Palindrome: ', string
    return True

for i in xrange(T):
    K = int(raw_input())
    n = int(math.sqrt(2*K))
    n = n if n*(n+1)/2.0 <= K else n-1
    k = n*(n+1)/2

    X = K - k

    if X == 0:
        print n
    else:
        sol = 'a'*n
        answer = try_all_combos(sol, K)
        print len(finalsol[0]) 
