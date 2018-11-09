from random import choice, randint, seed
from time import time

import graphics

def quicksort(lst, f=None, pivot=None):

    if len(lst) <= 1:
        return lst

    if not (f is None):
        pivot = f(lst)
        lst.remove(pivot)
    elif pivot is None:
        raise ValueError

#   print("pivot:", pivot)

    lst_lower = []
    lst_upper = []
    for n in lst:
#       print(type(n), type(pivot))
        if n < pivot:
            lst_lower.append(n)
        else:
            lst_upper.append(n)
#   print(lst_lower, lst_upper)
#   print("gello:", len(lst_upper), len(lst_lower))
    
    if not (f is None):
        return  quicksort(lst_lower, f=f) + [pivot] + quicksort(lst_upper, f=f)
    else:
        return  quicksort(lst_lower, pivot=lst_lower[len(lst_lower)//2]) + \
                [pivot] + \
                quicksort(lst_upper, pivot=lst_upper[len(lst_upper)//2])

l = [randint(0, 100) for i in range (1000)]
def f(lst):
#   print(len(lst))
    return lst[len(lst)//2]

print("in:", l)
print("out: ", quicksort(l, f))

