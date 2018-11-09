from q_sort1 import generate_list


class Graphics:

    def __init__(self, max_val=1000, min_val=0, print_size=100):
        self.max_val = max_val
        self.min_val = min_val
        self.print_size = print_size

    def generate(self, input_list):
        delta = len(input_list) // self.print_size
        output = ('=' * self.print_size) + '\n\n'

        for pos_y in range(self.max_val - self.min_val, 0, -1):

            for pos_x in range(0, len(input_list), delta):

                if pos_y <= input_list[pos_x]:
                    output += '|'

                else:
                    output += ' '

            output += '\n'

        output += '\n' + ('=' * self.print_size) + '\n\n\n'
        return output


def try_graphics():
    graphics = Graphics(100, 0, 100)

    print(graphics.generate(generate_list(100, 0, 200)))

try_graphics()