# Encoder & Decoder for Sudoku:

from itertools import chain, product
from string import ascii_lowercase, ascii_uppercase


from exactcover import Exactcover
from math import floor, sqrt

DIGITS = "123456789" + ascii_lowercase + ascii_uppercase
#   """Encodes a Sudoku in Ascii-art to datastructure.

#     :param problem: The Sudoku as a Ascii-art.
#     :return: Encoded Sudoku
#     """



def encode_sudoku_from_ascii(problem=None):
    """Encodes a Sudoku in Ascii-art to datastructure.

    Args:
        problem:
            The Sudoku in Ascii-art

    Returns:
        Encoded Sudoku
    """
    rows = problem.split()
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("All rows must have length "+ n)

    initial = [(i, j, d) for i, row in enumerate(rows)
               for j, d in enumerate(row) if 0 <= DIGITS.find(d) < n]
    return n, initial


def decode_sudoku_to_ascii(n, solution):
    """Encodes a Sudoku from complex Datastructure to Ascii-art.

    :param n: Sidelength of the Sudoku.
    :param solution: The Sudoku in complex Datastructure.
    """
    grid = [["."] * n for _ in range(n)]
    for i, j, d in solution:
        grid[i][j] = d
    return "\n".join("".join(row) for row in grid)

# Solver

def sudoku_solve(n=9, problem=(), m=None, random=False):
    if m is None:
        m = int(floor(sqrt(n)))
    if n <= 0 or len(DIGITS) < n or n % m:
        raise ValueError("Bad dimensions")
    if not all(0 <= DIGITS.find(d) < n and 0 <= i < n and 0 <= j < n for i, j, d in problem):
        raise ValueError("Bad problem")

    constraints = {(i, j, d): ((i, j), (d, "row", i), (d, "col", j), (d, "block",
                                                                      i // m, j//(n//m))) for i, j, d in product(range(n), range(n), DIGITS[:n])}

    return Exactcover(constraints, problem, random)


def matrix_to_exact(grid):
    out=[]
    n= len(grid)
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num!=0:
                out.append((i,j,str(num)))
    return n, out


def exact_to_matrix(n,prob):
    out=[[0 for i in range(n)] for j in range(n)]
    for elem in prob:
        out[elem[0]][elem[1]]=int(elem[2])

    return out


def asci_to_matrix(problem):
    rows = problem.split()
    n = len(rows)
    if any(len(row) != n for row in rows):
        raise ValueError("All rows must have length "+ n)
    out=[]
    for row in rows:
        out.append(list(row))
