# https://www.hackerrank.com/challenges/two-arrays

T = int(raw_input())

for i in xrange(T):
    l, K = map(int, raw_input().split())

    a = map(int, raw_input().split())
    b = map(int, raw_input().split())

    a.sort()
    b.sort(reverse=True)

#    print a
#    print b

    for j in xrange(l):
        if (a[j] + b[j]) < K:
            print 'NO'
            break
    else:
        print 'YES'
