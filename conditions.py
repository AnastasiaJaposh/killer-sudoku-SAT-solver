import globals as g;

def convert(k, r, c):
    return (k - 1)*(g.m**2) + r*g.m + c + 1

def unique_square_value_condition(file):
    f = open(file, "a")
    
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
    f.close()

def row_condition(file):
    f = open(file, "a")
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
    f.close()

def column_condition(file):
    f = open(file, "a")
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
    f.close()    

def block_offset_to_coordinate(x, y, p):
    return x * g.n + (p // g.n), y * g.n + (p % g.n)

def block_condition(file):
    # in each block we have at least 1 k and at most 1 k
    # I will represet each block with its x and y indices
    # in each block squares will be named this way as their offset to x*n and y*n (example when n = 3 and m = 9)
    # +0 +1 +2
    # +3 +4 +5
    # +6 +7 +8
    # so if we have lets say +5 offset, we can identify that the coordinates of this in the grid is x * n + (5 // g.n), y * n + (5 % g.n)

    f = open(file, "a")
    
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
    f.close()    


