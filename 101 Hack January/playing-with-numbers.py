from bisect import bisect_left

def binarySearch(neg, q, lo=0, hi=None):
    hi = hi if hi is not None else len(neg)
    pos = bisect_left(neg, q, lo, hi)
    return pos
        
N = int(raw_input())
a = map(int, raw_input().split())

Q = int(raw_input())
q = map(int, raw_input().split())

negSum = 0
posSum = 0

neg = []

negSumLength = 0

for i in xrange(N):
    if a[i] < 0:
        negSumLength += 1
        neg.append(a[i])
    else:
        posSum += a[i]

nL = negSumLength
neg.sort()
neg.reverse()

negSums = [neg[0]]
for i in xrange(1, nL):
    negSums.append(neg[i] + negSums[i-1])


negSum = negSums[-1]
#print neg
#print negSums

#print negSum, posSum, negSumLength, N - negSumLength    
for i in xrange(Q):
    q[i] += q[i-1] if i > 0 else 0

    idx = binarySearch(neg, -q[i], 0, nL-1)
    #print "b: " + str(binarySearch(neg, -q[i], 0, nL-1)) + " for q: " + str(q[i])

    negNew = negSums[idx] 
    sol = abs((idx) * q[i] + negNew)
    #print sol
    sol += abs((nL - idx) * q[i] + negSum - negNew)
    print nL, idx, q[i], negSum, negNew
    #print sol
    sol += (N - negSumLength) * q[i] + posSum
    #print sol

    print sol
