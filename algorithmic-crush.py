# https://www.hackerrank.com/challenges/crush

(N, M) = map(int, raw_input().split())

hashed = {}

abk = []

for i in xrange(M):
    x = map(int, raw_input().split())
    abk.append(x)

    

abk.sort(key=lambda x:x[2], reverse=True)


    
