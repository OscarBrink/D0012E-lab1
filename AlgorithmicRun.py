from random import choice, randint, seed
from math import log
from time import time

import graphics

operation_counter = 0
max_val = 10000
min_val = 0
size = 1000

def run_algorithm_gfx(function_to_run):
    g = graphics.Graphics(min_val, max_val, 100, 20)

    l = generate_list(min_val, max_val, size)

    print("NOT SORTED:\n" + g.generate(l))

    sorted_l = function_to_run(l)
    print("SORTED:\n" + g.generate(sorted_l))
    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))

def run_algorithm(function_to_run):
    l = generate_list(min_val, max_val, size)

    sorted_l = function_to_run(l)
    print("Sort check:", "passed" if is_sorted(sorted_l) else "failed")
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print(len(l), round(log(len(l), 2)))
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))

def run_algorithm_nopr(function_to_run):
    function_to_run(generate_list(min_val, max_val, size))
    return operation_counter

def median(function_to_run):
    l = generate_list(min_val, max_val, size)
    print(l)
    print(function_to_run(l))
    print(sorted(l, key=int))

def generate_list(min_val, max_val, size):
    return [randint(min_val, max_val) for i in range(size)]

def is_sorted(lst):
    prev = lst[0]
    for item in lst:
        if item < prev:
            return False
        prev = item
    return True

