# https://www.hackerrank.com/challenges/reverse-game

T = int(raw_input())

for i in xrange(T):
    N, K = map(int, raw_input().split())
    
    arr = range(0, N)
    sol = []
    
    j = 0
    k = N-1

    while k >= j:
        if k == j:
            sol.append(arr[k])
            break
        sol.extend([arr[k], arr[j]])
        k -= 1
        j += 1

    #print sol
    print sol.index(K)
