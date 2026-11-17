import globals as g;
import parse_input as p;

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

def format_combinations(cage, combinations):
    formatted_combinations = []
    for i in range(len(combinations)):
        l = []
        for j in range(len(combinations[i])):
            l.append((combinations[i][j], cage.squares[j][0], cage.squares[j][1])) # (k, i, j) tuple
        # print(*l)
        formatted_combinations.append(l[:])
    return formatted_combinations



def all_combinations(cage):
    # we have squares and we want to return all possible combinations 
    n = cage.count
    sum = cage.sum

    used = [False]*(g.m + 1)
    stack = []
    combinations = []
    def go(i, rem): # i := number of squares left in the cage, rem := sum of the remaining squares
        if i == 0:
            if rem == 0:
                # print(*stack)
                combinations.append(stack[:])
            return

        for j in range(1, g.m + 1): # we can't have more than g.m
            if used[j]:
                continue
            if rem - j < 0:
                break;
            stack.append(j)
            used[j] = True;
            go(i - 1, rem - j)
            stack.pop()
            used[j] = False

    
    go(n, sum)
    return format_combinations(cage, combinations)


def subsets(n, k):
    stack = []
    subsets = []

    def go(i): # the highest element in the stack, remaining count of elements
        if len(stack) == k:
            print(*stack)
            subsets.append(stack[:])
            return
        if i > n:
            return

        stack.append(i)
        go(i + 1) # add the element to the stack
        stack.pop()
        go(i + 1) # don't add the element to the stack
    go(1)

    return subsets
        

def cage_condition(file):
    # for the cage condition, we will calculate all possible combinations for each cage
    # and then use double implications for representing them, for example
    # if we have a cage of length 2(00, 01 squares) and sum 5 in 4x4 grid, we will write
    # p1,00 <-> p4,01; p4,00 <-> p1,01; p2,00 <-> p3,01; p3,00 <-> p2,01
    # p_k,ij means that k is on (i,j) square
    # lets say we have cage of length 3(00, 01, 02) and sum 9 in 9x9 grid
    # then for each combination we will have: (eg 1 2 6)
    # p1,00 <-> (p2,01 <-> p6,02)
    # p1,00 <-> (p2,02, <-> p6,01)
    # p2,00 <-> (p1,01 <-> p)
    
    # I practiced on online converters and saw this pattern
    # lets say we have p_1 <-> (p_2 <->(p_3 <-> .....(p_n-1 <-> p_n)))
    # if we convert it to cnf we will get these clauses
    # (n choose k) means that we choose k elementary variables to negate
    # if n even: (n choose 1) + (n choose 3) + (n choose 5) + ... + (n choose n - 1)
    # if n odd: (n choose 0) + (n choose 2) + (n choose 4) + ... + (n choose n - 1)

    # first we need to calculate all the possible combinations for the sum(ordering matters)
    # for cag in g.cages:
    #     combs = all_combinations(cag)
    #     print(*combs)
    # then take the variables and convert it to cnf
    # to do this, we need to calculate (n choose k) values, so all k-element subsets of {1, ..., n}
    pass

