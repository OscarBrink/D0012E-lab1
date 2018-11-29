from random import randint

def sub_partition(array, start, end, idx_pivot):

    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return array

    idx_pivot = randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    #print array, i, idx_pivot
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)

    return array

def LstGen(min,max,n):
    i=0
    lst =[]
    while(i<n):
        lst.append(randint(min,max))
        i = i+1
    return lst


