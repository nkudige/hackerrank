# https://www.hackerrank.com/contests/pythonista-practice-session/challenges/finding-the-percentage

N = int(raw_input())

students = {}

for i in xrange(N):
    ip = raw_input().split()
    marks = map(float, ip[1:])
    students[ip[0]] = marks

q = raw_input()
print "%.2f" % float(sum(students[q]) / 3)
