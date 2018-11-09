from random import choice
from AlgorithmicRun import run_algorithm, operation_counter


def quicksort(lst, f=None, pivot=None):
    global operation_counter

    # Base Case
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
        operation_counter += 1
        #       print(type(n), type(pivot))
        if n < pivot:
            lst_lower.append(n)
        else:
            lst_upper.append(n)
    #   print(lst_lower, lst_upper)
    #   print("gello:", len(lst_upper), len(lst_lower))

    if not (f is None):
        return quicksort(lst_lower, f=f) + [pivot] + quicksort(lst_upper, f=f)
    else:
        return quicksort(lst_lower, pivot=lst_lower[len(lst_lower) // 2]) + \
               [pivot] + \
               quicksort(lst_upper, pivot=lst_upper[len(lst_upper) // 2])


def f(lst): return lst[len(lst) // 2]


def f2(lst): return lst[len(lst) // 4]


def f3(lst): return choice(lst)


def to_run(l):
    return quicksort(l, f3)


run_algorithm(to_run)

# print("in:", l)
# print("out: ", quicksort(l, f))
