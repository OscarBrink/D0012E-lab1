from random import choice, randint
import AlgorithmicRun
import graphics
from math import ceil, sqrt


def sub_partition(lst, start, end, pivot_index):

    if not (start <= pivot_index <= end):
        raise ValueError("idx pivot must be between start and end")

    lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
    pivot = lst[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if lst[j] <= pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
        j += 1

    lst[start], lst[i - 1] = lst[i - 1], lst[start]
    return i - 1

def quicksort(lst, start=0, end=None, f=None):

    if end is None:
        end = len(lst) - 1

    if end - start < 1:
        return lst

#   index_pivot = randint(start, end)
    index_pivot = f(lst, start, end)
    i = sub_partition(lst, start, end, index_pivot)
    #print lst, i, index_pivot
    quicksort(lst, start, i - 1, f)
    quicksort(lst, i + 1, end, f)

    return lst

def middle_pivot(lst, start, end): return start + len(lst[start:end]) // 2


def random_pivot(lst, start, end): return start + randint(start, end)



def n_median_pivot(lst, start, end, amount):
    subl_len = end - start
    step = subl_len // (amount - 1)
    index = start
    elems = []

    if subl_len > amount:
        while index < subl_len:
            try:
                elems.append([lst[index], index])
                index += step
            except IndexError:
                break

        # If the length of list is even, the last elem has to be appended
        if len(elems) < amount and subl_len >= amount:
            elems.append([lst[end - 1], end - 1])
    else:
        # Copy lst into elems if smaller than amount
        for i in range(start, end):
            elems.append([lst[i], i])

    #   print("elems:", len(elems))
    # for now inefficient sort
    #   print(elems)

    # Insertion sorting the selected elements
    for i in range(len(elems)):
        j = i
        while j > 0 and elems[j][0] < elems[j - 1][0]:
            temp = elems[j - 1]
            elems[j - 1] = elems[j]
            elems[j] = temp
            j -= 1

    #   print(elems)
    #   print(elems[ceil(len(elems)/2) - 1])
    return elems[ceil(len(elems) / 2) - 1][1]


med_3 = lambda lst, start, end: n_median_pivot(lst, start, end, 3)
med_5 = lambda lst, start, end: n_median_pivot(lst, start, end, 5)
med_7 = lambda lst, start, end: n_median_pivot(lst, start, end, 7)


def to_run(l):
    return quicksort(l, f=med_3)


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
