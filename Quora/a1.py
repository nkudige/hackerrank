n = int(raw_input())
r = map(int, list(raw_input().split()))
m = int(raw_input())

count = 0

while m:
    x1, y1, x2, y2 = map(int, list(raw_input().split()))
    i = 0
    for i in range(n):
        if ((x1 * x1) + (y1 * y1)) < (r[i] * r[i]) and ((x2 * x2) + (y2 * y2)) > (r[i] * r[i]):
            count += 1
    m -= 1

print count
