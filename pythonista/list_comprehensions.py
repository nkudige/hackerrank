# https://www.hackerrank.com/contests/pythonista-practice-session/challenges/list-comprehensions

X,Y,Z,N = [int(raw_input()),int(raw_input()),int(raw_input()),int(raw_input())]

x = [a for a in xrange(X+1)]
y = [a for a in xrange(Y+1)]
z = [a for a in xrange(Z+1)]

res = []

for a in x:
    for b in y:
        for c in z:
            if a+b+c != N:
                res.append([a,b,c])

print res
