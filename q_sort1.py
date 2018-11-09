from random import choice

def quicksort(lst, f=None, pivot=None):

    if not (f is None):
        pivot = f(lst)
    elif pivot is None:
        raise ValueError

    lst1 = []
    lst2 = []
    for n in lst:
        lst

