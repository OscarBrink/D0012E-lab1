from random import choice, randint, seed
from time import time

from graphics import Graphics

def quicksort(lst, f=None, pivot=None):

    if not (f is None):
        pivot = f(lst)
    elif pivot is None:
        raise ValueError

    lst1 = []
    lst2 = []
    for n in lst:
        lst



def generate_list(max_val, min_val, list_size):
    seed(time())
    output = []

    for i in range(0, list_size):
        output.append(randint(min_val, max_val))

    return output

