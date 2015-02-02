def flip(b):
    res = ''
    for i in xrange(0, len(b)):
        res = res + '1' if b[i] == '0' else res + '0'
#    print res
    return res

T = int(raw_input())

for i in xrange(T):
    n = int(raw_input())
    b = bin(n)[2:]
    b = (32 - len(b))*'0' + b
#    print b

    print int(flip(b),2)

    
