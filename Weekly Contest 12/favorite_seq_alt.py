# https://www.hackerrank.com/contests/w12/challenges/favourite-sequence

def sort_it_out(x):
    solution = []
    for i in xrange(1002):
        t = set(solution).union(set(x[i]))
        if len(t) == len(solution) + len(x[i]):
            

    return solution

N = int(raw_input())

magic = []
[magic.append([]) for i in xrange(1002)]

for i in xrange(N):
    seq = map(int, raw_input().split())[1:]
    for (i, n) in enumerate(seq):
        magic[i].append(n)

for i in xrange(1002):
    for element in magic[i]:
        for k in xrange(i):
            magic[k] = filter(lambda a:a != element, magic[k])
        

for x in magic:
    if len(x)>0:
        print x


result = sort_it_out(magic)

#for i in xrange(len(result)):
#    print result[i],
