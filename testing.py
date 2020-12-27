from XSolver import sudoku_solve, encode_sudoku_from_ascii, decode_sudoku_to_ascii, matrix_to_exact, exact_to_matrix
import time
from testGrids import Grids


def foo():
    PROBLEM = '''
        ...84...9
        ..1.....5
        8...2146.
        7.8....9.
        .........
        .5....3.1
        .2491...7
        9.....5..
        3...84...
        '''

    n, problem = encode_sudoku_from_ascii(PROBLEM)
    # print(problem)
    print(decode_sudoku_to_ascii(9, next(sudoku_solve(n, problem))))


def boo():
    PROBLEM = '''
        ...84...9
        ..1.....5
        8...2146.
        7.8....9.
        .........
        .5....3.1
        .2491...7
        9.....5..
        3...84...
        '''

    n, problem = matrix_to_exact(Grids.grid16x16_3)
    # print(problem)
    # print()
    print(decode_sudoku_to_ascii(n, next(sudoku_solve(n=n, problem=problem))))


def poo():
    inp = [[[0, 0, '7'], [0, 3, '5'], [0, 7, '9'], [1, 2, '8'], [2, 0, '4'], [2, 1, '1'], [2, 4, '2'], [2, 5, '7'], [2, 8, '5'], [3, 1, '7'],
            [3, 4, '3'], [3, 5, '4'], [4, 0, '8'], [4, 8, '2'], [5, 3, '6'], [5, 4, '5'], [5, 7, '1'], [6, 0, '5'], [6, 3, '7'], [6, 4, '1'],
            [6, 7, '4'], [6, 8, '3'], [7, 6, '6'], [8, 1, '4'], [8, 5, '2'], [8, 8, '7']]]
    out = list(map(lambda inpp: list(map(tuple, inpp)), inp))
    print(out)


# prob = [(0, 3, '8'), (0, 4, '4'), (0, 8, '9'), (1, 2, '1'), (1, 8, '5'), (2, 0, '8'), (2, 4, '2'), (2, 5, '1'), (2, 6, '4'),
#         (2, 7, '6'), (3, 0, '7'), (3, 2, '8'), (3, 7, '9'), (5, 1, '5'), (5, 6, '3'), (5, 8, '1'), (6, 1, '2'), (6, 2, '4'),
#         (6, 3, '9'), (6, 4, '1'), (6, 8, '7'), (7, 0, '9'), (7, 6, '5'), (8, 0, '3'), (8, 4, '8'), (8, 5, '4')]

# n, problem = encode_sudoku_from_ascii(PROBLEM)
# print(problem)
# print(decode_sudoku_to_ascii(n, next(sudoku_solve(n, problem))))

# # foo()
# gr=Grids.grid9x9_1
# print(gr)
# print(matrix_to_exact())
poo()
