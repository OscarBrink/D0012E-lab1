from random import choice, randint, seed
from math import log, floor
from time import time

import graphics

operation_counter = 0
max_val = 10000
min_val = 0
size = 1000

def run_algorithm_gfx(function_to_run):
    g = graphics.Graphics(min_val, max_val, 275, 20)
#   g = graphics.Graphics(min_val, max_val, 100, 20)

    l = generate_list(min_val, max_val, size, 0)

    print("NOT SORTED:\n" + g.generate(l))

    sorted_l = function_to_run(l)
    print("SORTED:\n" + g.generate(sorted_l))
    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))
    return operation_counter

def run_algorithm(function_to_run, l):
    
    sorted_l = function_to_run(l)
    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))
    return operation_counter

def run_algorithm_nopr(function_to_run, l):
    function_to_run(l)
    return_value = operation_counter, 10
    operation_counter = 0
    return return_value

def median(function_to_run):
    l = generate_list(min_val, max_val, size)
    print(l)
    print(function_to_run(l))
    print(sorted(l, key=int))

# Generates a list that is rando
def generate_list(min_val, max_val, size, complexity = 0):

    complexity = max(min(1, complexity), 0)

    delta = (max_val - min_val) / size
    output = []

    for i in range(size):
        output.append(floor(i * delta * complexity + \
                randint(min_val, max_val) * (1 - complexity)))

    return output

#def calculate_inversion(input_list):
#    counter = 0
#
#    for i in range(len(input_list) - 1):
#        counter += 1 if input_list[i] > input_list[i + 1] else 0
#
#    return counter / len(input_list)

def calculate_inversion(input_list):
    counter = 0
    ops = 0

    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            counter += 1 if input_list[i] > input_list[j] else 0
            ops += 1
    print(ops)

    return counter / ( ( len(input_list) * (len(input_list) - 1) ) // 2)


def is_sorted(lst):
    prev = lst[0]
    for item in lst:
        if item < prev:
            return False
        prev = item
    return True

def generate_lst_to_file(file_name, lists_to_generate, **kwargs):
    for key in ("err", "max_val", "min_val", "size", "tries", "continue_on_fail"):
        if key not in kwargs:
            raise ValueError

    lists = []
    print(len(lists_to_generate), "lists to generate")
    lst_no = 1

    for x in lists_to_generate:
        print(lst_no)

        complexity = 0.5 + (x * 0.5)

        # Attempt construction 3 times
        for i in range(1, kwargs["tries"] + 1):

            print("Complexity:", complexity, "attempt:", i)
            lst = generate_list(
                    kwargs["min_val"], kwargs["max_val"], kwargs["size"], x
            )

            inversion = 1.0 - calculate_inversion(lst)
            print("inversion:", inversion)

            if complexity - kwargs["err"] \
                    <= inversion\
                    <= complexity + kwargs["err"]:

                lists.append(lst)

                print("List with complexity:", complexity, "done at", i, "tries.")
                break

            else:
                print("Complexity:", complexity, "failed")
        lst_no += 1

    if len(lists) == 0:
        print("No lists to write")
        raise ValueError # TODO better exception

    with open(file_name, "wb") as f:
        f.write(len(lists).to_bytes(4, "little"))
        for lst in lists:
            f.write(len(lst).to_bytes(4, "little"))
            for i in lst:
                f.write(i.to_bytes(4, "little"))


def test():
    generate_lst_to_file(
            "out.bin",
            [0.25, 0.0, 0.5],
            err=0.1,
            min_val=0, max_val=1000000, size=100,
            tries=10, continue_on_fail=True
    )

#   read_lists = []
#   with open("out.bin", "rb") as f:
#       amount = int.from_bytes(f.read(4), "little")
#       for i in range(amount):
#           length = int.from_bytes(f.read(4), "little")
#           l = []
#           for i in range(length):
#               l.append(int.from_bytes(f.read(4), "little"))
#           read_lists.append(l)



#   g = graphics.Graphics(0, 1000, 275, 70)
#   l = generate_list(0, 1000, 1000, 0.25)
#
#   print(g.generate(l))
#   print(1.0 - calculate_inversion(l))

test()
