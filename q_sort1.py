from random import choice
import AlgorithmicRun


def quicksort(lst, f=None, pivot=None):

    # Base Case
    if len(lst) <= 1:
        return lst

    AlgorithmicRun.operation_counter += 1

    if not (f is None):
        pivot = f(lst)
        lst.remove(pivot)
    elif pivot is None:
        raise ValueError

    # General case
    lst_lower = []
    lst_upper = []
    for n in lst:
        if n < pivot:
            lst_lower.append(n)
        else:
            lst_upper.append(n)

    # Concatenate the two quicksorts
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


AlgorithmicRun.run_algorithm(to_run)

