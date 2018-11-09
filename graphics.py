class Graphics:

    def __init__(self, max_val=1000, min_val=0, print_size=100):
        self.max_val = max_val
        self.min_val = min_val
        self.print_size = print_size

    def generate(self, input_list):
        delta = len(input_list) // self.print_size
        output = ''

        for pos_y in range(self.max_val - self.min_val):

            for pos_x in range(0, len(input_list), delta):

                if pos_y <= input_list[pos_x]:
                    output += '|'

                else:
                    output += ' '

            output += '\n'

        return output



