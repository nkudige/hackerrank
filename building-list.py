# https://www.hackerrank.com/challenges/building-a-list


import itertools
 
def powerset(s):
    """powerset('abc') -> a b c ab ac bc abc"""
    for chars in itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(1, len(s)+1)
        ):
        yield ''.join(chars)

T = int(raw_input())

for i in xrange(T):
    raw_input()
    s = raw_input()
    
    sets = [''.join(sorted(x)) for x in powerset(s)]
    sets = sorted(sets)

    for item in sets:
        print item
