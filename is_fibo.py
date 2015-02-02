#https://www.hackerrank.com/challenges/is-fibo

T = int(raw_input())
fib = [1, 1]
n = 1

def isFibo(x):
    global fib, n
    
    if x in fib:
        return True
    elif x < fib[n]:
        return False
    else:
        while fib[n] < x:
            a, b = fib[n-1], fib[n]
#            print a, b
            n += 1
            fib.append(a+b)
          
        print fib
        return True if fib[n] == x else False

for i in xrange(T):
    N = int(raw_input())
    
    print 'IsFibo' if isFibo(N) else 'IsNotFibo'
