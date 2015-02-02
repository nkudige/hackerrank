def sumIt(n):
    return n*(n+1)/2

(N, K) = map(int, raw_input().split())
upvotes = map(int, raw_input().split())

for i in xrange(N-K+1):

    nonI = 0
    nonIT = 0
    nonD = 0
    nonDT = 0

    first = True
    f = 0
    
    for j in xrange(i+1, i+K):
        if upvotes[j] >= upvotes[j-1]:
            nonI += 1
        elif nonI > 0:
            nonIT += sumIt(nonI)
            if first:
                f = nonI
                first = False
            nonI = 0

        if upvotes[j] <= upvotes[j-1]:
            nonD += 1
        elif nonD > 0:
            nonDT += sumIt(nonD)
            nonD = 0
            
    nonIT += sumIt(nonI)
    nonDT += sumIt(nonD)
    
    print nonIT - nonDT
