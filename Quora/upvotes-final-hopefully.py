#https://www.hackerrank.com/contests/quora-haqathon/challenges/upvotes

(N, K) = map(int, raw_input().split())
upvote = map(int, raw_input().split())

uvInc = []
uvDec = []

cSeqInc = 0
cSeqDec = 0

for i in xrange(0, N-1):
    if upvote[i] <= upvote[i+1]:
        cSeqInc += 1
    else:
        uvInc.append(cSeqInc)
        if cSeqInc != 0:
            uvInc.append(0)
        cSeqInc = 0

    if upvote[i] >= upvote[i+1]:
        cSeqDec += 1
    else:
        uvDec.append(cSeqDec)
        if cSeqDec != 0:
            uvDec.append(0)
        cSeqDec = 0

uvInc.append(cSeqInc)
uvDec.append(cSeqDec)

print uvInc
print uvDec
