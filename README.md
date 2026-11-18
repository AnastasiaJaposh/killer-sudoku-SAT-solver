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
After receiving an input in the correct format, it will encode the problem into a CNF formula in DIMACS CNF format in file temp/formula.cnf, then the script runs the Glucose 4.2 SAT-solver on this formula, outputting the raw results into temp/result.txt. The results will be decoded and printing to temp/solution.txt file, which will be simply numbers in a grid put correctly or UNSAT, which means that it is not solvable.

## Correct input format
Killer Sudoku start grid has no numbers inserted already, thus we define the input with cages.
It should look like this
> *{n}*\
> *{number of cages}*\
> *{arbitrary amount of lines defining cages}*

Note: n is the square root of grid width/height, so we will have n^2 X n^2 grid.\
Lines defining cages should be in this format:\
> *{sum}* *{number of squares in the cage}* *{list of squares, delimited by space character, 0-indexed row and column indices left-padded with zeros(if needed) and concatenated}*

padding is needed if there is variable number of digits for an index.

An examples of a correct input format for lines defining cages:
> 5 2 00 01 // not padded\
> 10 3 0200 0300 0301 // padded

## Running the script
To run the script, run the main method "main.py" with the argument being the name of file, with correct input.\
<code>python3 main.py input.in</code>

## Encoding into CNF
Proposition for number k, being on row i and column j is calculated the following way:
> (k - 1)(n^4) + i*(n^2) + j + 1

This way each proposition 1,...,n^3 is taken.

For rules 1,...,4 mentioned above, I calculate the formulas the following way
1. At least 1 k in the square/row/column/block
2. At most 1 k in the square/row/column/block

The cage rule, is done by a different approach. The non-model approach is used. First all possible m-tuple combinations of numbers is calculated, and then they are filtered out, such that the combination is not satisfactory for the solved problem. Then we negate each variable and calculate the conjuncture.

## Provided instances
In the file there are total of 6 instances provided. They can be viewed in ./instances/ directory:
1. trivial_grid1x1.in - n = 1
2. grid_2.in - easily checked solvable solution
3. grid_unsat_2.in - easily checked unsolvable solution
4. grid_3.in - 9x9 solvable grid which is calculated fast
5. grid_3_harder.in - 9x9 solvable grid, which takes more time to be calculated, because the cages are bigger
6. grid_4.in - 16x16 grid, which takes too long to compute(wouldn't recommend running it, just for demonstration)

## Conducted experiments
All results mentioned here can be found in the directory: ./results/
