# https://www.hackerrank.com/challenges/utopian-tree

T = int(raw_input())
lengths = [1] * 61

def treeLength(N):
    global lengths

    if lengths[N] > 1:
        return lengths[N]

    x = 0
    
    for i in xrange(N, -1, -1):
        if lengths[i] > 1:
            x = i
            break

    length = lengths[x]
    
    for i in xrange(x, N):
        if i % 2 == 0:
            length *= 2
        else:
            length += 1

    lengths[N] = length
    return length

for i in xrange(T):
    N = int(raw_input())
    print treeLength(N)
