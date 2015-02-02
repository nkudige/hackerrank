s = raw_input()

alpha = [False]*26

n = len(s)

for i in xrange(n):
    x = ord(s[i].lower()) - 97
    if x >= 0 and x <=25 and not alpha[x]:
        alpha[ord(s[i].lower()) - 97] = True
    if alpha == [True]*26:
        break
else:
    print 'not',

print 'pangram'
