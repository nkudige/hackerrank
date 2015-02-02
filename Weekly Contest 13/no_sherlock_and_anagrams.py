from collections import Counter

def unordered_anagrams(string):
    x = len(string)
    c = 0
    for i in xrange(1, x):
        for k in xrange(x):
            word = string[k:k+i]
            for j in xrange(k+1, x):
                newWord = string[j:i+j]
                if Counter(word) == Counter(newWord):
                    c += 1
                    #print word, newWord

    return c

T = int(raw_input())

for i in xrange(T):
    string = raw_input()

    n = unordered_anagrams(string)

    print n
