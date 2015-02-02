class Tree(object):
    def __init__(self):
        self.left = False
        self.right = False
        self.data = 0

N = int(raw_input())
nodes = [Tree() for i in xrange(N)]

data = map(int, raw_input().split())

for i in xrange(N-1):
    nodes[i].data = data[i]
    
    (m, n) = map(int, raw_input().split())
    m -= 1
    n -= 1
    
    if not nodes[m].left:
        nodes[m].left = nodes[n]
    elif not nodes[m].right:
        nodes[m].right = nodes[n]
        
nodes[N-1].data = data[N-1]

total = sum(data)

tree_diff = total
x, y = -1, -1

for 

