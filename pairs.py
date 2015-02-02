# https://www.hackerrank.com/challenges/pairs

N, K = map(int, raw_input().split())
arr = map(int, raw_input().split())

arr.sort()

idx = 0
idx2 = 1

c = 0

if N < 2:
    print 0

else:
    while idx < N:
#        print idx, idx2
        if arr[idx2] - arr[idx] == K:
            c += 1
            idx += 1

        elif idx2 == N-1:
            idx += 1
            
        elif arr[idx2] - arr[idx] < K:
            idx2 += 1
        
        elif arr[idx2] - arr[idx] > K:
            idx += 1

    print c
