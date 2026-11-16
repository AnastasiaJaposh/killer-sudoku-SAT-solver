# n
# #_of_cages
# lines defining cages:
# sum #_of_blocks __ __ __ } blocks, seperated by spaces

import globals as g;

class cage:
    def __init__(self, sum, count, input):
        self.sum = sum;
        self.count = count
        self.squares = [];
        for i in input:
            self.add_square(i);
        

    def add_square(self, padded_coefficients):
        if len(self.squares) >= self.count:
            return
        row, column = int(padded_coefficients[:len(padded_coefficients)//2]), int(padded_coefficients[len(padded_coefficients)//2:])
        self.squares.append((row, column))
        
        
def parse(filepath):
    f = open(filepath, "r")
    g.n = int(f.readline())
    g.m = g.n * g.n
    cage_count = int(f.readline())
    for i in range(cage_count):
        l = f.readline().split()
        g.cages.append(cage(int(l[0]), int(l[1]), l[2:]))
    f.close()

# parse_input("small_grid2x2.in")
# for c in g.cages:
#     print(f"sum = {c.sum}, count  = {c.count}, squares = ", end="")
#     print(*c.squares)

        

