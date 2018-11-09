from random import choice, randint, seed
from time import time

import graphics

operation_counter = 0

def run_algorithm(function_to_run):
    g = graphics.Graphics(10000, 0, 100, 20)

    l = generate_list(0, 10000, 1000)

    print("NOT SORTED:\n" + g.generate(l))

    print("SORTED:\n" + g.generate(function_to_run(l)))
    print("Size:", len(l))
    print("Comparisons:", operation_counter)


def generate_list(min_val, max_val, size):
    return [randint(min_val, max_val) for i in range(size + 1)]