def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        n = len(list)-1
        pivot = list[n]
        lesser = qsort1([x for x in list[0:n] if x < pivot])
        greater = qsort1([x for x in list[0:n] if x >= pivot])
        print lesser + [pivot] + greater
        return lesser + [pivot] + greater

N = int(raw_input())
list = map(int, raw_input().split())
qsort1(list)
