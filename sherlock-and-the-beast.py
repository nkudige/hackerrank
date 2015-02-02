# https://www.hackerrank.com/challenges/sherlock-and-the-beast

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())

    done = False
    if N%3 == 0:
        print '%s' % '5'*N
        done = True

    else:
        n = N + (3 - N%3)
        while n >= 0:
            
            n -= 3
            if (N-n)%5 == 0 and (N-n) <= N:
                print '%s' % '5'*n + '3'*(N-n)
                done = True
                break

    if not done:
        print -1
