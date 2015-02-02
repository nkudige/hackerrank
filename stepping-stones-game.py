# https://www.hackerrank.com/challenges/stepping-stones-game

def is_reachable(n):
    root = int((n*2)**0.5)
    if root*(root+1)/2 == n:
        return root
    elif (root+1)*(root+2)/2 == n:
        return root+1
    else:
        return -1
    

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())

    possible = is_reachable(N)
    if possible == -1:
        print 'Better Luck Next Time'
    else:
        print 'Go On Bob', possible
