from itertools import islice
from random import sample
from XSolver import sudoku


class AmbiguousProblem(Exception):
    pass
class ImpossibleProblem(Exception):
    pass



def solve_sudoku(n=9, problem=(), m=None):

    sols = list(islice(sudoku(n, problem, m), 2))
    if len(sols) == 1:
        return sols[0]
    elif len(sols) == 0:
        raise ImpossibleProblem('no sols')
    else:
        raise AmbiguousProblem('two or more sols')

def make_sudoku(n=9, m=None):
    solution = sorted(next(sudoku(n=n, m=m, random=True)))
    given = [True] * n**2
    k = (n**2 + 1) // 2
    for i in sample(range(k), k):
        given[i] = given[-i-1] = False
        p = [solution[j] for j, g in enumerate(given) if g]
        try:
            solve_sudoku(n, p, m)
            problem = p
        except AmbiguousProblem:
            given[i] = given[-i-1] = True
    return problem