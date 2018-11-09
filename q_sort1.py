from random import choice

def quicksort(lst, f=None, pivot=None):

    if not (f is None):
        pivot = f(lst)
    elif pivot is None:
        raise ValueError

    lst_lower = []
    lst_upper = []
    for n in lst:
        if n < pivot:
            lst_lower.append(n)
        else:
            lst_upper.append(n)
    
    if not (f is None):
        pivot = f(lst)
    elif pivot is None:
        raise ValueError

