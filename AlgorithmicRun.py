from random import choice, randint, seed
from math import log, floor
from time import time

import graphics

operation_counter = 0
run_time = 0
max_val = 10000
min_val = 0
size = 1000
#Självkommenterande kod
def run_algorithm_gfx(function_to_run):
    global run_time
    g = graphics.Graphics(min_val, max_val, 275, 20)
#   g = graphics.Graphics(min_val, max_val, 100, 20)

    l = generate_list(min_val, max_val, size, 0.0)

    print("NOT SORTED:\n" + g.generate(l))
    print("Sort check:", "passed" if is_sorted(l) else "failed")

    last_time = time()
    sorted_l = function_to_run(l)
    run_time = int((time() - last_time) * 1000)

    print("SORTED:\n" + g.generate(sorted_l))
    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))
    return operation_counter

def run_algorithm(function_to_run, l):
    global run_time

    last_time = time()
    sorted_l = function_to_run(l)
    run_time = int((time() - last_time) * 1000)

    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))
    return operation_counter

def run_algorithm_nopr(function_to_run, l):
    global operation_counter
    global run_time
    
    last_time = time()
    sorted_l = function_to_run(l)
    run_time = int((time() - last_time) * 1000)

    return_value = operation_counter, run_time
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
    #print(ops)

    return counter / ( ( len(input_list) * (len(input_list) - 1) ) // 2)


def is_sorted(lst):
    prev = lst[0]
    for item in lst:
        if item < prev:
            return False
        prev = item
    return True

def generate_lst_to_file(file_name, lists_to_generate, **kwargs):
    for key in ("err", "max_val", "min_val", "size", "tries", "amount_per_compl"):
        if key not in kwargs:
            raise ValueError

    compls = []
    print(len(lists_to_generate), "compls to generate")
    print(kwargs["amount_per_compl"], "lists per compl")
    compl_no = 1
    lst_no = 1

    for x in lists_to_generate:
        print("complno:", compl_no)
        lists = []
        for n in range(kwargs["amount_per_compl"]):
            print("lstno:", lst_no)

            complexity = 0.5 + (x * 0.5)

            # Attempt construction 3 times
            for i in range(1, kwargs["tries"] + 1):

                print("Complexity:", complexity, "attempt:", i)
                lst = generate_list(
                        kwargs["min_val"], kwargs["max_val"], kwargs["size"], x
                )

                #inversion = 1.0 - calculate_inversion(lst)
                inversion = complexity
                print("inversion:", inversion)

                if complexity - kwargs["err"] \
                        <= inversion \
                        <= complexity + kwargs["err"]:

                    lists.append((inversion, lst))

                    print("List with complexity:", complexity, "done at", i, "tries.")
                    break

                else:
                    print("Complexity:", complexity, "failed")

            lst_no += 1

        compls.append(lists)
        compl_no += 1

    if len(compls) == 0:
        print("No lists to write")
        raise ValueError # TODO better exception

    for i in range(len(compls)):
        if len(compls[i]) == 0:
            print("No lists to write at compl", lists_to_generate[i])
            raise ValueError # TODO better exception

    with open(file_name, "wb") as f:
        # write amount of compls
        f.write(len(compls).to_bytes(4, "little"))

        for i in range(len(compls)):
            # write nominal complexity
            nominal_complexity = int(lists_to_generate[i] * 1000000)
            f.write(nominal_complexity.to_bytes(4, "little"))
            # write amount of lists in compl
            f.write(len(compls[i]).to_bytes(4, "little"))

            for lst in compls[i]:
                # write real complexity
                real_complexity = int(lst[0] * 1000000)
                f.write(real_complexity.to_bytes(4, "little"))
                # write length of list (amount of elems)
                f.write(len(lst[1]).to_bytes(4, "little"))
                for j in lst[1]:
                    # write elements
                    f.write(j.to_bytes(4, "little"))

#   return compls # TODO remove


def test():
#   compls = generate_lst_to_file(
#           "out.bin",
#           [0.0, 0.5, 0.95],
#           err=0.1,
#           min_val=0, max_val=1000000, size=100,
#           tries=10, amount_per_compl=10
#   )

    generate_lst_to_file(
            "out2.bin",
            [0.0, 0.25, 0.5, 0.75, 0.95, 1.0],
            err=0.03,
            min_val=0, max_val=1000000, size=100000,
            tries=60, amount_per_compl=10
    )

#   read_compls = []
#   with open("out.bin", "rb") as f:
#       len_compls = int.from_bytes(f.read(4), "little")
#       for i in range(len_compls):
#           nominal_compl = int.from_bytes(f.read(4), "little")
#           len_lists = int.from_bytes(f.read(4), "little")
#           lists = []
#           for j in range(len_lists):
#               real_compl = int.from_bytes(f.read(4), "little")
#               len_list = int.from_bytes(f.read(4), "little")
#               l = []
#               for k in range(len_list):
#                   l.append(int.from_bytes(f.read(4), "little"))
#               lists.append((real_compl, l))
#           read_compls.append(lists)
#
#   print(bool_test(compls, read_compls))


#def bool_test(compl_1, compl_2):
#    if len(compl_1) != len(compl_2):
#        print("compl_len")
#        return False
#    for i in range(len(compl_1)):
#        if len(compl_1[i]) != len(compl_2[i]):
#            print("lists_len")
#            return False
#        for j in range(len(compl_1[i])):
#            if len(compl_1[i][j]) != len(compl_2[i][j]):
#                print("list_len")
#                return False
#           if compl_1[i][j][0] != compl_2[i][j][0]:
#               print("real_compl")
#               return False
#            for k in range(len(compl_1[i][j][1])):
#                if compl_1[i][j][1][k] != compl_2[i][j][1][k]:
#                    print("element")
#                    return False
#    return True


#   g = graphics.Graphics(0, 1000, 275, 70)
#   l = generate_list(0, 1000, 1000, 0.25)
#
#   print(g.generate(l))
#   print(1.0 - calculate_inversion(l))

#test()
