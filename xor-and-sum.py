# https://www.hackerrank.com/challenges/xor-and-sum

def operate(a, b):
    s = 0

    x = len(bin(a)) - 2
    y = bin(a)
    y = y[2:]

    c = 0
    
    for i in xrange(x):
        c = (a ^ (b << i))
        s = (s + c) % 1000000007
#        print s

    c = bin(c)[2:-len(y)]
#    print c
    for i in xrange(x, 314159 + 1):
        c = c + '0'
        s += int(c+y, 2)
#        print s

##    for i in xrange(314159 + 1):
##        b = b << 1
##        s += (a ^ b)
##        s %= 1000000007

    
        
    return s

a = int(raw_input(), 2)
b = int(raw_input(), 2)

res = operate(a, b)
print res % 1000000007

