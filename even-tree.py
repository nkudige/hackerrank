# https://www.hackerrank.com/challenges/even-tree

def updateCounts(hashed, children, node):
    x = 0
    for child in children.get(node, []):
        x += (1 + updateCounts(hashed, children, child))
        
    hashed[node] = x
    return x
            
def prune(hashed, children, parent, node):
    global count
    for child in children.get(node, []):
        prune(hashed, children, parent, child)

    t = hashed.get(node, -1)

    if t == -1:
        return

    if not t % 2 == 0 and not parent.get(node, -1) == -1:
        count += 1
        hashed[parent[node]] -= (t+1)

    return

    

[N, M] = map(int, raw_input().split())

hashed = {}
children = {}
parent = {}

for i in xrange(M):
    [u, v] = map(int, raw_input().split())
    c = children.get(v, [])
    c.append(u)
    children[v] = c
    parent[u] = v

updateCounts(hashed, children, 1)

count = 0
prune(hashed, children, parent, 1)

#print children
#print hashed
print count
