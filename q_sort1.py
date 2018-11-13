from random import choice
import AlgorithmicRun
import graphics

from time import sleep


def quicksort(lst, f=None, pivot=None):
    # Base Case
    if len(lst) <= 1:
        return lst

    if not (f is None):
        pivot = f(lst)
        lst.remove(pivot)
    elif pivot is None:
        raise ValueError

    # General case
    lst_lower = []
    lst_upper = []
    for n in lst:
        AlgorithmicRun.operation_counter += 1
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


def quicksort2(lst, pivot=None):
    # Base Case
    if len(lst) <= 1:
        return lst

    if pivot is None:
        pivot = lst[len(lst) // 2]

    # General case
    lst_lower = []
    lst_upper = []

    lst_lower_sum = 0
    lst_upper_sum = 0

    for n in range(len(lst)):
        AlgorithmicRun.operation_counter += 1

        lst_active = lst_lower if lst[n] < pivot else lst_upper
        lst_active_sum = lst_lower_sum if lst[n] < pivot else lst_upper_sum

        if lst_active_sum == 0 or len(lst_active) == 0:
            lst_active_sum = lst[n]
            lst_active.append(lst[n])

        else:

            if lst_active_sum / len(lst_active) > lst[n]:
                lst_active = [lst[n]] + lst_active  # TODO: Change operators

            else:
                lst_active = lst_active + [lst[n]]

            lst_active_sum += lst[n]

        if lst[n] < pivot:
            lst_lower = lst_active
            lst_lower_sum = lst_active_sum

        else:
            lst_upper = lst_active
            lst_upper_sum = lst_active_sum

    if len(lst) == 1000:
        g = graphics.Graphics(0, 1000, 100, 100)

        print('Upper\n' + g.generate(lst_lower))
        print('Lower\n' + g.generate(lst_upper))

    # Concatenate the two quicksorts
    return quicksort2(lst_lower) + [pivot] + quicksort2(lst_upper)


def f(lst): return lst[len(lst) // 2]


def f2(lst): return lst[len(lst) // 4]


def f3(lst): return choice(lst)


def to_run(l):
    # return quicksort(l, f3)
    # return quicksort2(l)
    return quicksort3(l)


def kinda_sort(l):
    max_val = None
    min_val = None

    output = []

    for i in range(len(l)):
        AlgorithmicRun.operation_counter += 1
        instance = l[i]

        if max_val is None or min_val is None:
            max_val = max(instance, 0)
            min_val = min(instance, 0)

            output.append(instance)

        else:

            try:
                position = instance / ((max_val - min_val) // len(output))

                if position >= len(output):
                    output.append(instance)
                elif position <= 0:
                    output.insert(0, instance)
                else:
                    output.insert(position, instance)

            except:

                if l[-1] < instance:
                    output.append(instance)
                else:
                    output.insert(0, instance)

    return output


def quicksort3(l, pivot=None):
    if len(l) <= 1:
        return l

    if pivot is None:
        pivot_value = (AlgorithmicRun.max_val - AlgorithmicRun.min_val) // 2
        first_instance = True
    else:
        pivot_value = l[pivot]
        first_instance = False

    lower_pivot = 0
    upper_pivot = 0

    lower = []
    upper = []

    for i in range(len(l)):
        if pivot is None or i != pivot:
            AlgorithmicRun.operation_counter += 1
            instance = l[i]

            if instance < pivot_value:

                if lower_pivot is 0 or abs(pivot_value * 0.5 - instance) < abs(
                        pivot_value * 0.5 - lower[lower_pivot]):
                    lower_pivot = len(lower)

                lower.append(instance)

            else:

                if upper_pivot is 0 or abs(pivot_value * 1.5 - instance) < abs(
                        pivot_value * 1.5 - upper[upper_pivot]):
                    upper_pivot = len(upper)

                upper.append(instance)
    print("pivot:", pivot_value)
    print("lower:", len(lower), lower_pivot)
    try: print(lower[lower_pivot]) 
    except IndexError: print("empty")
    print("upper:", len(upper), upper_pivot)
    try: print(upper[upper_pivot]) 
    except IndexError: print("empty")
    print()

    return quicksort3(lower, lower_pivot) + ([pivot_value] if not first_instance else []) + quicksort3(upper, upper_pivot)


AlgorithmicRun.max_val = 10000
AlgorithmicRun.min_val = 0
try:
    AlgorithmicRun.run_algorithm(to_run)
except KeyboardInterrupt:
    print("Oscar Keyboard-interruptade")
except IndexError:
    print("IndexError")
