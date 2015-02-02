#https://www.hackerrank.com/challenges/cut-the-sticks

N = int(raw_input())
lengths = map(int, raw_input().split())

lengths.sort()

while len(lengths) > 0:
    print len(lengths)
    lengths = [y for y in lengths if y != lengths[0]]
