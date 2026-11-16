import globals as g;

def convert(k, r, c):
    return (k - 1)*(g.m**2) + r*g.m + c + 1

def unique_square_value_condition(file):
    # forall r,c pairs at least 1 and at most 1 value should be assigned
    f = open(file, "a")

    # at least one
    at_least_one = ""
    for i in range(g.m):
        for j in range(g.m):
            for k in range(1, g.m + 1):
                at_least_one += f"{convert(k, i, j)} "
            f.write(at_least_one + "0\n")
            g.formulas_count += 1
            at_least_one = ""

    # at most one
    for i in range(g.m):
        for j in range(g.m):
            for k in range(1, g.m + 1):
                for l in range(k + 1, g.m + 1):
                    f.write(f"-{convert(k, i, j)} -{convert(l, i, j)} 0\n")
                    g.formulas_count += 1
    f.close()
