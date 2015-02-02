# https://www.hackerrank.com/challenges/lexicographic-steps

from math import factorial

T = int(raw_input())

for i in range(T):
    (x,y,K)=map(int,raw_input().split())

    result = "H"*x + "V"*y
    
    if K==0:
        print result
    else:
        K = K + 1   
        result = ""
        
        while x > 0 and y > 0:
            paths = factorial(x-1+y) / factorial(x-1) / factorial(y)
            
            if K <= paths:
                
                result += "H"
                x -= 1
                
            else:
                
                result += "V"

                K = K - paths
                y = y - 1
                
        result += "H" * x + "V" * y
        
        print result
        
    
    
