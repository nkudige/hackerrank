import math
t = int(raw_input())
while t>0:
    t-=1
    d,p=map(int,list(raw_input().split()))
    k=0
    if d<0:
        print 0
        continue
    if d*d+4*p>=-0:    
        k=math.sqrt(d*d+4*p)
    else:
        print 0
        continue
    count=0
    if p==0 and d==0:
        print 1
        continue
    if p==0:
        print 4
        continue
    if k==int(k):
        if (d+k)%2 == 0:
            count+=2
        if (-d+k)%2 == 0 and d!=0:
            count+=2
    print count
