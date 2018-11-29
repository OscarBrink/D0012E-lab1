from random import choice
import AlgorithmicRun
import graphics
from math import ceil, sqrt


def quicksort(lst, f=None, start=0, end=None):

    if end is None:
        end = len(lst) - 1

    if end - start == 2:
        if lst[start] > lst[end - 1]:
            lst[start], lst[end - 1] = lst[end - 1], lst[start]
            AlgorithmicRun.operation_counter += 1
    if end - start <= 2:
        return lst[start:end]

    try:
        pivot_index = lst.index(f(lst[start:end]))
    except ValueError:
        print("Pivot value is not an element of lst")
        return

    lst[pivot_index], lst[start] = lst[start], lst[pivot_index]
    pivot_index = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[pivot_index]:
            lst.insert(pivot_index, lst.pop(i))
            pivot_index += 1
            AlgorithmicRun.operation_counter += 1

    return quicksort(lst, f, start, pivot_index) + quicksort(lst, f, pivot_index, end)


def temp2(lst):
    return lst[len(lst) // 2]


def quicksort2(lst, f=None):
    # Base Case
    if len(lst) <= 1:
        return lst

    pivot = f(lst)
    pivot_index = lst.index(pivot)
    lst.remove(pivot)

    # General case
    lst_lower = []
    lst_upper = []
    for n in lst:
        AlgorithmicRun.operation_counter += 1
        if n < pivot:
            lst_lower.append(n)
        else:
            lst_upper.append(n)

    lst.insert(pivot_index, pivot)

    # Concatenate the two quicksorts
    return quicksort(lst_lower, f=f) + [pivot] + quicksort(lst_upper, f=f)


def middle_pivot(lst): return lst[len(lst) // 2]


def random_pivot(lst): return choice(lst)


def n_median_pivot(lst, amount):
    #   print("len:", len(lst))
    step = len(lst) // (amount - 1)
    index = 0
    elems = []

    if len(lst) > amount:
        while index < len(lst):
            try:
                elems.append(lst[index])
                index += step
            except IndexError:
                break

        # If the length of list is even, the last elem has to be appended
        if len(elems) < amount and len(lst) >= amount:
            elems.append(lst[-1])
    else:
        # Copy lst into elems if smaller than amount
        elems = lst[:]

    #   print("elems:", len(elems))
    # for now inefficient sort
    #   print(elems)

    # Insertion sorting the selected elements
    for i in range(len(elems)):
        j = i
        while j > 0 and elems[j] < elems[j - 1]:
            temp = elems[j - 1]
            elems[j - 1] = elems[j]
            elems[j] = temp
            j -= 1

    #   print(elems)
    #   print(elems[ceil(len(elems)/2) - 1])
    return elems[ceil(len(elems) / 2) - 1]


med_3 = lambda lst: n_median_pivot(lst, 3)
med_5 = lambda lst: n_median_pivot(lst, 5)
med_7 = lambda lst: n_median_pivot(lst, 7)


def to_run(l):
    return quicksort(l, middle_pivot)

#   return quicksort(l, random_pivot)
def shite():
    AlgorithmicRun.max_val = 1000000
    AlgorithmicRun.min_val = 0
    AlgorithmicRun.size = 100000

    try:
        AlgorithmicRun.run_algorithm_gfx(to_run)
    #   AlgorithmicRun.median(lambda lst : n_median_pivot(lst, 3))
    except KeyboardInterrupt:
        print("Keyboard-interrupt")
    except IndexError:
        print("IndexError")
    return

shite()