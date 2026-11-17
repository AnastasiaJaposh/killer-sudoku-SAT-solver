import globals as g


def convert_back(p):
    p = p - 1
    k = p // (g.m**2) + 1

    p = p % (g.m * g.m)
    i = p // g.m
    j = p % g.m
    return (k, i, j)


def decode(file):
    grid = [[[] for i in range(g.m)] for i in range(g.m)]
    f = open(file, "r")
    for literal in f.readline().split():
        p = int(literal)
        if(p <= 0):
            continue

        (k, r, c) = convert_back(p)
        grid[r][c] = k

    f.close()
    return grid

def print_grid(file, grid):
    f = open(file, "w")
    for r in grid:
        for c in r:
            f.write(f"{c} ")
        f.write("\n")

    f.close()
    
