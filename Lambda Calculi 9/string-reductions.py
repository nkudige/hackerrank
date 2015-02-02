#https://www.hackerrank.com/contests/lambda-calculi-9/challenges/string-reductions

s = raw_input()

included = [False]*26

res = ""

for char in s:
    if not included[ord(char)-97]:
        res += char
        included[ord(char)-97] = True

    if not False in included:
        break

print res
