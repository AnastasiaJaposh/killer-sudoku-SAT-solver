import globals as g;
import parse_input as p;

def encode(file):
    f = open(file, "w+")
    f.write("                                            ") # I should have enough spaces to prepend the first line, without messing up the formulas
    unique_square_value_condition(f)
    row_condition(f)
    column_condition(f)
    block_condition(f)
    cage_condition(f)

    f.seek(0,0)
    f.write(f"p cnf {g.m**3} {g.formulas_count}\n")
    f.close()



def convert(k, r, c):
    return (k - 1)*(g.m**2) + r*g.m + c + 1

def unique_square_value_condition(f):
    # f = open(file, "a")
    
    at_least_one = ""
    # at most one
    for i in range(g.m):
        for j in range(g.m):
            for k in range(1, g.m + 1):
                at_least_one += f"{convert(k, i, j)} "
                for l in range(k + 1, g.m + 1):
                    f.write(f"-{convert(k, i, j)} -{convert(l, i, j)} 0\n")
                    g.formulas_count += 1
            f.write(at_least_one + "0\n")
            g.formulas_count += 1
            at_least_one = ""

def row_condition(f):
    # f = open(file, "a")
    at_least_one = ""

    for k in range(1, g.m + 1):
        for i in range(g.m):
            for j in range(g.m):
                at_least_one += f"{convert(k, i, j)} "
                for l in range(j + 1, g.m):
                    f.write(f"-{convert(k, i, j)} -{convert(k, i, l)} 0\n")
                    g.formulas_count += 1
            f.write(at_least_one + "0\n")
            g.formulas_count += 1
            at_least_one = ""
    # f.close()

def column_condition(f):
    # f = open(file, "a")
    at_least_one = ""


    for k in range(1, g.m + 1):
        for j in range(g.m):
            for i in range(g.m):
                at_least_one += f"{convert(k, i, j)} "
                for l in range(i + 1, g.m):
                    f.write(f"-{convert(k, i, j)} -{convert(k, l, j)} 0\n")
                    g.formulas_count += 1
            f.write(at_least_one + "0\n")
            g.formulas_count += 1
            at_least_one = ""
    # f.close()    

def block_offset_to_coordinate(x, y, p):
    return x * g.n + (p // g.n), y * g.n + (p % g.n)

def block_condition(f):
    # in each block we have at least 1 k and at most 1 k
    # I will represet each block with its x and y indices
    # in each block squares will be named this way as their offset to x*n and y*n (example when n = 3 and m = 9)
    # +0 +1 +2
    # +3 +4 +5
    # +6 +7 +8
    # so if we have lets say +5 offset, we can identify that the coordinates of this in the grid is x * n + (5 // g.n), y * n + (5 % g.n)

    # f = open(file, "a")
    
    at_least_one = ""
    for k in range(1, g.m + 1):
        for x in range(g.n):
            for y in range(g.n): # block identified
                for p in range(g.m):
                    at_least_one += f"{convert(k, block_offset_to_coordinate(x, y, p)[0], block_offset_to_coordinate(x, y, p)[1])} "
                    for l in range(p + 1, g.m):
                        g.formulas_count += 1
                        f.write(f"-{convert(k, block_offset_to_coordinate(x, y, p)[0], 
                                    block_offset_to_coordinate(x, y, p)[1])} -{convert(k, block_offset_to_coordinate(x, y, l)[0], 
                                    block_offset_to_coordinate(x, y, l)[1])} 0\n") # for each pair of squares, either not first or not second
                f.write(at_least_one + "0\n")
                g.formulas_count += 1
                at_least_one = ""
    # f.close()    

def is_valid(cage, assignment):
    return cage.sum == sum(assignment) and len(set(assignment)) == len(assignment) # no duplicate elements

def every_combination(cage):
    stack = []
    combs = []

    def go():
        if len(stack) == cage.count:
            combs.append(tuple(stack))
            return

        for i in range(1, g.m + 1):
            stack.append(i)
            go()
            stack.pop()

    go()
    return combs



def cage_condition(f):
    # another approach is to use the models to convert to cnf
    # lets say we have cage of sum 7 and count 2 in 9x9 grid:
    # 1 6, 2 5, 3 4, 6 1, 5 2, 4 3. the models would be corresponding to these
    # to convert it to cnf, we should compute all non-models
    # 1 1, 1 2, 1 3, 1 4, 1 5, 2 1, 2 2, ...
    # and the use the negated variables
    # first calculate all digit combinations which is (1,1), (1,2) etc for count 2
    # then determine if they are valid
    # if they arent valid negate each variable and add to the file
    for cag in g.cages:
        for combination in every_combination(cag): # combination would be (1,1) or (1,2) etc
            if(is_valid(cag, combination)):
                continue

            formula = ""
            for i in range(cag.count):
                formula += f"-{convert(combination[i], cag.squares[i][0], cag.squares[i][1])} "
            f.write(formula + "0\n")
            g.formulas_count += 1
    
