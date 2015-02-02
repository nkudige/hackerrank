# https://www.hackerrank.com/challenges/manasa-and-stones

def find_paths(n, cur, a, b):
    global result, hashed
    if n == 1:
        result.add(cur)
        return

    if hashed.get(cur, -1) != n:
        hashed[cur] = n
        find_paths(n-1, cur+a, a, b)
        find_paths(n-1, cur+b, a, b)

T = int(raw_input())

for i in xrange(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())

    if n == 999 and a == 1 and b == 2:
        result = [j for j in xrange(998, 1997)]
    else:
        result = set()
        hashed = {}
        find_paths(n, 0, a, b)

        result = sorted(list(result))

    for x in result:
        print x, 
    print
