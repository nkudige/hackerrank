N = int(raw_input())

T = map(int, raw_input().split())
T = [(i+1, T[i]) for i in xrange(N)]

c = {}
tree = {}

for i in xrange(N-1):
    (A, B) = map(int, raw_input().split())
    c[A] = c.get(A, 0) + 1
    c[B] = c.get(B, 0) + 1

    branches = tree.get(A, [])
    branches.append(B)
    tree[A] = branches

    branches = tree.get(B, [])
    branches.append(A)
    tree[B] = branches

T.sort(key = lambda x: x[1])
print c
print tree
print T
