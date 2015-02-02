# https://www.hackerrank.com/challenges/halloween-party

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())

    print (N/2)**2 if N % 2 == 0 else (N/2)*(N/2 + 1)
