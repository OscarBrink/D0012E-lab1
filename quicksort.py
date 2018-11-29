from random import choice, randint
import AlgorithmicRun
import graphics
from math import ceil, sqrt

def quicksort(lst, f=None, start=0, end=None):
    if end is None:
        end = len(lst)

    if end - start < 1:
        return lst

    elif end - start < 2:
        if lst[start] > lst[end - 1]:
            lst[start], lst[end - 1] = lst[end - 1], lst[start]
        AlgorithmicRun.operation_counter += 1

        return lst

    try:
        pivot_index = f(lst, start, end)
        # print(lst[start:end])
        # print(sorted(lst[start:end]))
        # print(pivot_index, lst[pivot_index])
    except ValueError:
        # print("Pivot value is not an element of lst")
        return

    lst[pivot_index], lst[start] = lst[start], lst[pivot_index]
    pivot_index = start
    temp = lst[start:end + 1]

    for i in range(start + 1, end):
        if lst[i] <= lst[pivot_index]:
            lst.insert(pivot_index, lst.pop(i))
            if pivot_index < end:
                pivot_index += 1
            AlgorithmicRun.operation_counter += 1

    # lst[pivot_index], lst[start] = lst[start], lst[pivot_index]
    quicksort(lst, f, start, pivot_index)
    quicksort(lst, f, pivot_index, end)

    if end == len(lst) and start == 0:
        if lst[-2] > lst[-1]:
            lst[-1], lst[-2] = lst[-2], lst[-1]

        print(lst)

    return lst


def middle_pivot(lst, start, end): return start + len(lst[start:end]) // 2


def random_pivot(lst, start, end): return start + randint(start, end)


def n_median_pivot(lst, start, end, amount):
    lst = lst[start:end]
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
    return ceil(len(elems) / 2) - 1


med_3 = lambda lst: n_median_pivot(lst, 3)
med_5 = lambda lst: n_median_pivot(lst, 5)
med_7 = lambda lst: n_median_pivot(lst, 7)


def to_run(l):
    return quicksort(l, middle_pivot)


#   return quicksort(l, random_pivot)
def test_run():
    AlgorithmicRun.max_val = 100000
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


test_run()
