def longest(x, i, j):
    global table
    
    if table[i][j] > -1:
        return table[i][j]
    
    if j-i <= 0:
        table[i][j] = j-i+1
        return table[i][j]
    elif x[i] == x[j]:
        table[i][j] = 2+longest(x, i+1, j-1)
        return table[i][j]
    else:
        return max(longest(x, i+1,j),longest(x, i,j-1))

def build_table(x, n):
    table = [[-1 for i in xrange(n)] for j in xrange(n)]

    for i in xrange(n):
        for j in xrange(n):
            if j == i:
                table[i][j] = 1
            elif j < i:
                table[i][j] = 0

    print table
    
    for size in xrange(2, n):
        for i in xrange(n):
            j = i + size - 1
            if j >= n:
                break
            if i == 0 and j == 3:
                print i, j
            table[i][j] = table[i][j-1] if x[i] != x[j] else table[i][j-1] + 1
        
    print table

s = raw_input()

n = len(s)
m = 0

build_table(s, n)
    
print m
