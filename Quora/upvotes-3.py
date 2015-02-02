def sumIt(n):
    return n*(n+1)/2

(N, K) = map(int, raw_input().split())
upvotes = map(int, raw_input().split())

inc = [0]
dec = [0]

for i in xrange(1, N):
    if upvotes[i] > upvotes[i-1]:
        inc.append(inc[i-1] + 1)
    else:
        inc.append(0)

    if upvotes[i] < upvotes[i-1]:
        dec.append(dec[i-1] + 1)
    else:
        dec.append(0)

print inc
print dec

orderI = [sumIt(inc[K-1])]
orderD = [sumIt(inc[K-1])]

for i in xrange(1,N-K+1):
    print "i: ", i
    orderI.append(sumIt(inc[i+K-1]-inc[i-1]) - orderI[i-1])

for i in xrange(1,N-K+1):
    orderD.append(sumIt(dec[i+K-1]-inc[i-1]) - orderD[i-1])

print orderI
print orderD

##
##for i in xrange(N-K+1):
##
##    nonI = 0
##    nonIT = 0
##    nonD = 0
##    nonDT = 0
##    
##    for j in xrange(i+1, i+K):
##        if upvotes[j] >= upvotes[j-1]:
##            nonI += 1
##        elif nonI > 0:
##            nonIT += sumIt(nonI)
##            nonI = 0
##
##        if upvotes[j] <= upvotes[j-1]:
##            nonD += 1
##        elif nonD > 0:
##            nonDT += sumIt(nonD)
##            nonD = 0
##            
##    nonIT += sumIt(nonI)
##    nonDT += sumIt(nonD)
##    
##    print nonIT - nonDT
