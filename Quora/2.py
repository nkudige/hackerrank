N = int(raw_input())

jobs = []
for i in xrange(N):
    jobs.append(tuple(map(float, raw_input().split())))

jobs.sort(key = lambda x:x[1])

res = jobs[0][0] * (1-jobs[0][1])
t = jobs[0][0]
suc = jobs[0][1]

for i in xrange(1, N-1):
    t += jobs[i][0]
    res += t * suc*(1 - jobs[i][1])
    suc *= jobs[i][1]

print res + (t+jobs[-1][0])*suc
