# https://www.hackerrank.com/challenges/cipher

import timing

N, K = map(int, raw_input().split())
cipher = map(int, list(raw_input()))
              
#print cipher, N, K
sol = [cipher[0]]
XOR = cipher[0]

k = 0
for i in xrange(1, N):
    k += 1
    bit = cipher[i] if XOR == 0 else abs(cipher[i] - 1)
    
    sol.append(bit)
    XOR ^= bit

#    XOR = 0 if (bit == 0 and XOR == 0) or (bit == 1 and XOR == 1) else 1
    if k >= K-1:
        XOR ^= sol[k-K+1]
#        XOR = 0 if (sol[K-1] == 0 and XOR == 0) or (sol[K-1] == 1 and XOR == 1) else 1
        

#sol = sol[K-1:]

print "%s" % ''.join(map(str,sol))
