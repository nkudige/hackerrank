# https://www.hackerrank.com/challenges/runningtime

N = int(raw_input())

arr = map(int, raw_input().split())

c = 0
for i in xrange(1, N):
    flag = False
    j = i
    while j >= 0:
        j -= 1
        if j == -1:
            break
#        print i, j
        if arr[i] < arr[j]:
            flag = True
            c += 1
#            print c
        else:
            break
    if flag:
        arr2 = []
        arr2.extend(arr[:j+1])
        arr2.append(arr[i])
        arr2.extend(arr[j+1:i])
        arr2.extend(arr[i+1:])
        arr = arr2
#        print arr2
print c
