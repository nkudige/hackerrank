#https://www.hackerrank.com/challenges/stockmax

T = int(raw_input())
   
def solver(stocks):
    n = len(stocks) - 1
    x = 0

    profit = 0

    while len(stocks) > 0:
        m = max(enumerate(stocks), key = lambda x: x[1])
        profit += (m[1]*(m[0])) - sum(stocks[:m[0]])
        stocks = stocks[m[0]+1:]
#        print stocks, profit, x
        
    return profit

for i in xrange(T):
    N = int(raw_input())

    stocks = map(int, raw_input().split())

    profit = solver(stocks)
    print profit
