# https://www.hackerrank.com/challenges/almost-sorted

def isSorted(a, n):
    for i in xrange(n-1):
        if a[i] > a[i+1]:
            return False
    return True

def can_swap(a, n):
    anomalies = []
    anomalyCount = 0
    i = 0
    while i < n:
        if a[i] > a[i+1]:
            anomalyCount += 1
 #           print i, a[i], a[i+1]
            if anomalyCount > 2:
                return False
            anomalies.append(i)
        i += 1

    if anomalyCount == 1:
        anomalies.append(n-1)

    x = anomalies[0]
    
    if anomalies[1] == n-1:
        y = anomalies[1]
        a[anomalies[0]], a[anomalies[1]] = a[anomalies[1]], a[anomalies[0]]
    else:
        y = anomalies[1]+1
        a[anomalies[0]], a[anomalies[1]+1] = a[anomalies[1]+1], a[anomalies[0]]
        
    return [True, x+1, y+1] if isSorted(a, n) else False

def is_almost_sorted(a, i):
    j = i
    while j < N-1:
        if a[j] < a[j+1]:
            break

        j += 1

    return [False] if a[i] > a[j+1] or a[j] < a[i-1] else [True, a[i], a[j], i+1, j+1]
    #return [max, min, iIdx, jIdx]
    

N = int(raw_input())

a = map(int, raw_input().split())

i = 0
times = 0

almost_sorted = True

result = can_swap(a + [1000001], N)

if not result:

    while i < N-1:
        if a[i] > a[i+1]:
            times += 1
            if times > 1:
                almost_sorted = False
                break
            result = is_almost_sorted(a + [1000001], i)

            if not result[0]:
#                print max, a[jIdx+1]
#                print min, a[i-1]
                almost_sorted = False
                break

            i = result[4]-1
            
        i += 1

    if not almost_sorted:
        print 'no'
    else:
        print 'yes'
        print 'reverse', result[3], result[4]

else:
    print 'yes'
    print 'swap',result[1],result[2]
