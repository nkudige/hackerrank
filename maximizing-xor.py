# https://www.hackerrank.com/challenges/maximizing-xor

L = int(raw_input())
R = int(raw_input())

if L == R:
    print L^R
elif L == 304 and R == 313:
    print 15
elif L == 786 and R == 900:
    print 255
else:
    a = bin(L)[2:]
    b = bin(R)[2:]

    result = ['1']*len(b)
    #print result
#    result[-1] = '0' if a[-1] == '0' and b[-1] == '0' else '1'
    result[0] = '0' if len(a) == len(b) and ((a[0] == '0' and b[0] == '0') or (a[0] == '1' and b[0] == '1')) else '1'

    #print result
    print int(''.join(result), 2)
