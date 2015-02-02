# https://www.hackerrank.com/challenges/cipher

def xor(l):
    x = l[0]
    ln = len(l)
    for i in xrange(1, ln):
        x ^= l[i]
    return x

N, K = map(int, raw_input().split())
cipher = map(int, list(raw_input()))
              
#print cipher, N, K
sol = [cipher[N+K-2]]
#XOR = [cipher[N+K-2]]
lastBit = cipher[N+K-2]
XOR = lastBit

for i in xrange(N+K-3, -1, -1):
    x = xor(XOR[:K-1])
    bit = cipher[i] if x == 0 else abs(cipher[i] - 1)
    XOR = [bit] + XOR
    sol = [bit] + sol

for i,bit in enumerate(sol):
    if bit == 1:
        sol = sol[i:]
        break

print "%s" % ''.join(map(str,sol))
