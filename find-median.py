# https://www.hackerrank.com/challenges/find-median

n = int(raw_input())
print sorted(map(int, raw_input().split()))[n/2]
