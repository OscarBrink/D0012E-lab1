# A class (Yea, sorry. We used a class in python) to visualize the current list in the terminal
class Graphics:

    def __init__(self, max_val=1000, min_val=0, print_size_x=100, print_size_y=100):
        # The highest value that the values in the list can have
        self.max_val = max_val

        # The lowest value that the values in the list can have
        self.min_val = min_val

        # The width of the visualised output
        self.print_size_x = print_size_x

        # The height of the visualised output
        self.print_size_y = print_size_y

    def generate(self, input_list):
        # A delta value of the steps between the indexes in the input
        # list that should be outputted
        delta_x = len(input_list) // self.print_size_x

        # A delta value of the height of the graph,
        # that is used to split values in a defined
        # range
        delta_y = (self.max_val - self.min_val) // self.print_size_y

        output = ('=' * (self.print_size_x + 1)) + '\n\n'

        # Goes through every possible line that
        # can be outputted and checks if the
        # value on the index is higher than
        # that value
        for pos_y in range(self.max_val - self.min_val, 0, -1 * max(delta_y, 1)):

            for pos_x in range(0, len(input_list), max(delta_x, 1)):

                if pos_y <= input_list[pos_x]:
                    output += '|'

                else:
                    output += ' '

            output += '\n'
        output += '\n' + ('=' * (self.print_size_x + 1)) + '\n\n\n'
        return output
