import sys
import globals as g
import conditions as c
import parse_input as p

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

p.parse(inp)

f = open(outp, "a+")
f.write(f"p cnf {g.m**3} {g.formulas_count}\n") # I will set this later
f.close()

c.unique_square_value_condition(outp)
c.row_condition(outp)
c.column_condition(outp)
