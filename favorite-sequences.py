# https://www.hackerrank.com/contests/w12/challenges/favourite-sequence

def sort_it_out(x):
    solution = []
    for i in xrange(1002):
        if len(x[i]) > 0:
            solution.extend(sorted(list(x[i])))

    return solution

N = int(raw_input())

magic = []
[magic.append(set()) for i in xrange(1002)]

for i in xrange(N):
    seq = map(int, raw_input().split())[1:]
    for (i, n) in enumerate(seq):
        magic[i].add(n)

for i in xrange(1002):
    for element in magic[i]:
        for k in xrange(i):
            if element in magic[k]:
                magic[k].remove(element)
        

result = sort_it_out(magic)

##for x in magic:
##    if len(x)>0:
##        print x

for i in xrange(len(result)):
    print result[i],
