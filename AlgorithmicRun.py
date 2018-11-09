from random import choice, randint, seed
from math import log
from time import time

import graphics

operation_counter = 0
max_val = 10000
min_val = 0

def run_algorithm(function_to_run):
    g = graphics.Graphics(min_val, max_val, 100, 20)

    l = generate_list(min_val, max_val, 1000)

    print("NOT SORTED:\n" + g.generate(l))

    print("SORTED:\n" + g.generate(function_to_run(l)))
    print("Size:", len(l))
    print("Comparisons:", operation_counter)
    print("\nlog2(n)*n:", round(log(len(l), 2) * len(l)))


def generate_list(min_val, max_val, size):
    return [randint(min_val, max_val) for i in range(size + 1)]
