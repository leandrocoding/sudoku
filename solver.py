import math
import numpy as np
import random
import copy
import inspect


# Dimensions of the board variable?
# By default it should be 9x9
# The field can be bigger it however has to follow the rule, that the inner field is allways the squareroot tall and wide of the whole field.
# Example:
# Normal sudoku inner Fileds: 3x3, outer field is made out of 3x3 of the inner fields
# smaller Sudoku: inner field made out of 2X2 outer field is made of 2x2 of the outer field
# large Sudoku: inner field 4x4 outer field 16x16 or made out of 4x4 of the inner field.


# The size of the inner field
basesize = 3

# A board is defined as Colloms in Rows.   x=col y=row cords are in the format bo [row][col] or bo[y][x]
# A "0" stands dor empty.
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

board2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

temp = []


# Checking if it is possible to put a number at a certain point.


def check(num, row, col, bo):
    # Check Row
    if num in bo[row]:
        return False
    # Check Col
    for i in range(0, (basesize ** 2)):
        if num == bo[i][col]:
            return False
    # Check Square
    return checksquare(num, row, col, bo)

    return True


def checksquare(num, row, col, bo):
    squarerow = math.floor(row/3)
    squarecol = math.floor(col/3)
    rows = []
    cols = []
    for i in range(0, basesize):
        rows.append(squarerow*basesize + i)
        cols.append(squarecol*basesize + i)

    for roww in rows:
        for coll in cols:
            if bo[roww][coll] == num:
                return False
    return True


def solutioncounter(bo, debug=False):
    solutions = []
    solve(bo, sols=solutions)
    if len(solutions) == 1:
        print("There was a unique solution!")
    else:
        print(f"\nThere were {len(solutions)} solutions")

    if debug:

        for solu in solutions:
            print("\n")
            print(np.matrix(solu))


def solve(bo, sols=temp, testuni=False):

    for row in range(0, basesize**2):
        for col in range(0, basesize**2):
            # Find empty field
            if bo[row][col] == 0:
            
                for n in range(1, basesize**2+1):
                    if check(n, row, col, bo):
                        bo[row][col] = n
                        if solve(bo, sols) == "FINITO":
                            return "FINITO"
                        bo[row][col] = 0
                # print(len(inspect.stack(0)))
                # if len(inspect.stack(0)) >= 40:
                #     return "FINITO"
                return

    sols.append(bo)

    if len(sols) > 1:
        return "FINITO"


def solvable(bo):
    solus = []
    solve(board2, sols=solus, testuni=True)
    if len(solus) == 0:
        return False
    else:
        return True


def solved(bo):
    for row in range(basesize**2):
        for col in range(basesize**2):
            if bo[row][col] == 0:
                return False
    return True


def isUnique(bo):
    solus = []
    solve(board2, sols=solus, testuni=True)
    if len(solus) == 1:
        return True
    else:
        return False


def generateSudoku(seed=None):
    if seed == None:
        seed = random.randint(1, 100000000000000000000)

    grid = [[0 for i in range(basesize**2)]for j in range(basesize**2)]

    i = 14
    gSudoku(seed, grid, i)
    if solved(grid):
        return grid


def gSudoku(seed, grid, i):

    random.seed(a=seed+135+57*i)
    row = random.randint(0, basesize**2-1)
    random.seed(a=seed+655+13*i)
    col = random.randint(0, basesize**2-1)
    random.seed(a=seed+575+67*i)
    num = random.randint(1, basesize**2)
    if grid[row][col] == 0:
        if check(num, row, col, grid):
            grid[row][col] = num
            if not solvable(grid):
                grid[row][col] = 0
            print(np.matrix(grid))
            gSudoku(seed, grid, i+3)
            # grid[row][col] = 0
        return
    if solved(grid):
        return grid
    gSudoku(seed, grid, i+3)
    # if not solvable(grid):
    #     print("Not solvable")


    # Testing
temp = generateSudoku(1243132413)
print(np.matrix(temp))
# solutioncounter(temp)

# if solve(board2, sols=solus, testuni=True) == "FINITO":
#     print(f"More than one Solution found")
# print(more)


# solutioncounter(board)

# grid2 = [[0 for i in range(basesize**2)]for j in range(basesize**2)]
# print(np.matrix(grid2))
# print(np.matrix(board))

# solutioncounter(grid2)
