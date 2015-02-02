# https://www.hackerrank.com/challenges/hamming-distance

def do_swaps(S, l1, r1, l2, r2):
    new_S = ''.join(S)
    first_segment = S[l1:r1+1]
    second_segment = S[l2:r2+1]
    new_S = S[:l1] + second_segment + S[r1+1:l2] + first_segment + S[r2+1:]

    return list(new_S)

N = int(raw_input())
S = ['']
S.extend(list(raw_input()))
#print S
M = int(raw_input())

for i in xrange(M):
    query = raw_input().split()

    if query[0] == 'C':
        S[int(query[1]):int(query[2])+1] = query[3] * (int(query[2])+1 - int(query[1]))
#        print ''.join(S[1:])

    elif query[0] == 'S':
        l1, r1, l2, r2 = int(query[1]), int(query[2]), int(query[3]), int(query[4])
        S = do_swaps(S, l1, r1, l2, r2)
#        print ''.join(S[1:])

    elif query[0] == 'R':
        S[int(query[1]):int(query[2])+1] = [ch for ch in reversed(S[int(query[1]):int(query[2])+1])]
#        print ''.join(S[1:])
        
    elif query[0] == 'W':
        print ''.join(S[int(query[1]):int(query[2])+1])

    elif query[0] == 'H':
        l1, l2, le = int(query[1]), int(query[2]), int(query[3])
        c = 0
        for j in xrange(le):
            if S[l1+j] != S[l2+j]:
                c += 1
        print c
