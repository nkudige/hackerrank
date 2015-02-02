# https://www.hackerrank.com/challenges/polar-angles

from math import atan
from math import degrees

N = int(raw_input())

angles = []

for i in xrange(N):
    (x, y) = map(int, raw_input().split())

    angle = 0
    if x == 0:
        angle = 90 if y > 0 else angle
        angle = 270 if y < 0 else angle

    elif y == 0:
        angle = 0 if x > 0 else angle
        angle = 180 if x < 0 else angle

    else:
        angle = degrees(atan(float(y)/x))

        angle = 180+angle if y < 0 and x < 0 else angle
        angle = 360+angle if y < 0 and x > 0 else angle
        angle = 180+angle if y > 0 and x < 0 else angle
    
    angles.append((x, y, angle))

angles.sort(key = lambda x:(x[2], x[1]**2, x[0]**2))

for angle in angles:
    print angle[0], angle[1]
