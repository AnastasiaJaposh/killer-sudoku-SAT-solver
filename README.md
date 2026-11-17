# killer-sudoku-SAT-solver

Killer Sudoku is a problem involing an NxN grid, where N is a perfect square.\
At first we are given an empty grid, with cages defined.

*cage*: A set of adjacent squares in the grid, with designated sum\
*block*: A Sqrt(N) X Sqrt(N) aligned subgrid

The solution will be inserting a number 1,...,N in each block, so that:
1. There is an unique number on each square
2. In each row, numbers aren't repeated
3. In each column, numbers aren't repeated
4. In each block, the numbers aren't repeated
5. The sum of number in each cage adds up to the sum of that cage
6. In each cage, the numbers aren't repeated

### Quick access
- Motivation
- Correct input format
- Running the script
- Encoding into CNF
- Provided instances
- Results for the provided instances

## Motivation
After receiving an input in the correct format, it will encode the problem into a CNF formula in DIMACS CNF format in file temp/formula.cnf, then the script runs the Glucose 4.2 SAT-solver on this formula, outputting the raw results into result.txt. The results will be decoded and printing to temp/solution.txt file, which will be simply numbers in a grid.
