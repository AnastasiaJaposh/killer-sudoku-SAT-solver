import sys
import subprocess
import globals as g
import conditions as c
import parse_input as p
import decode_result as d

inp = sys.argv[1]

# parse the input
p.parse(inp)

# calculate the cnf formula
c.encode(g.formula)

# run the glucose sat solver
subprocess.run(["./glucose", f"{g.formula}",  f"{g.result}"])

# decode the result and print in the solution file
try:
    d.print_grid(g.solution, d.decode(g.result))
except:
    print("UNSAT")


