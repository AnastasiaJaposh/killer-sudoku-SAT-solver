import sys
import subprocess
import globals as g
import conditions as c
import parse_input as p
import decode_result as d

# let m = n^2
# let k be the value {1 ,..., m}
# let r, c represent rows and columns respectively
# p_k,r,c denoting that k is or is not on the position (r,c)
# p_k,r,c = (k - 1)*(m*m) + r*m + c + 1
#
# the DIMACS cnf file should start with p cnf m**3
#
# row condition
# column condition
# block condition
# cage condition



inp = sys.argv[1]
outp = "formula.cnf"
result = "result.txt"
solution = "solution.txt"

# parse the input
p.parse(inp)


# calculate the cnf formula
f = open(outp, "w+")
f.write("                                            ") # I should have enough spaces to prepend the first line, without messing up the formulas
c.unique_square_value_condition(f)
c.row_condition(f)
c.column_condition(f)
c.block_condition(f)
c.cage_condition(f)

f.seek(0,0)
f.write(f"p cnf {g.m**3} {g.formulas_count}\n")
f.close()

# run the glucose sat solver
subprocess.run(["./glucose", f"{outp}",  f"{result}"])

# decode the result and print in the solution file
d.print_grid(solution, d.decode(result))
