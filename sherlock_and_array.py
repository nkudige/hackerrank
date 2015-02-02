# https://www.hackerrank.com/challenges/sherlock-and-array

T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    a = map(int, raw_input().split())

    lsum = [0]
    for j in xrange(1, N):
        lsum.append(lsum[j-1] + a[j-1])

    rsum = [0]*N
    for j in xrange(N-2, -1, -1):
        rsum[j] = rsum[j+1] + a[j+1]

    #print lsum
    #print rsum

    for j in xrange(0, N):
        if lsum[j] == rsum[j]:
            print 'YES'
            break
    else:
        print 'NO'
