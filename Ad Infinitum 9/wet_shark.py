#https://www.hackerrank.com/contests/infinitum9/challenges/wet-shark-and-42

T = int(raw_input())

for i in xrange(T):
    S = int(raw_input())

    res = S*2
    forty_two_steps = res / 42
    temp = forty_two_steps
    while temp != 0:
 #       print forty_two_steps, temp, res
 #       raw_input()
        res += temp*2

        temp = res / 42 - forty_two_steps
        forty_two_steps = res / 42
    
    print res % 1000000007
