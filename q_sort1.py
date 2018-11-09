from random import choice, randint, seed
from time import time

import graphics

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



def generate_list(max_val, min_val, list_size):
    seed(time())
    output = []

    for i in range(0, list_size):
        output.append(randint(min_val, max_val))

    return output

