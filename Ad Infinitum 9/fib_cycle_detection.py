from math import sqrt

def fib(n):
    phi = (1 + sqrt(5))/2
    p = (1 - sqrt(5))/2

    return int((pow(phi, n) - pow(p, n))/(phi - p))

##f = [0, 1, 1]
##l = 3
##
##i = 3
##while True:
##    x = fib(i)
##    i += 1

n=int(raw_input())
s=[]
a=k=0
b=1
while s[:k] != s[k:] or k < 1:
    s.append(a % n);
    k=len(s)/2;
    a,b=b,a+b
print k
