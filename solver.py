import math
# import numpy as np
import random
import copy
import inspect
from time import sleep
from config import basesize, currGrid, solving, sleeptime


# Dimensions of the board variable?
# By default it should be 9x9
# The field can be bigger it however has to follow the rule, that the inner field is allways the squareroot tall and wide of the whole field.
# Example:
# Normal sudoku inner Fileds: 3x3, outer field is made out of 3x3 of the inner fields
# smaller Sudoku: inner field made out of 2X2 outer field is made of 2x2 of the outer field
# large Sudoku: inner field 4x4 outer field 16x16 or made out of 4x4 of the inner field.


# # The size of the inner field
# basesize = config.basesize

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

possibleNumbers = []
for i in range(basesize**2+1):
    possibleNumbers.append(i)


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



def checksquare(num, row, col, bo):
    squarerow = math.floor(row/basesize)
    squarecol = math.floor(col/basesize)
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


def solutioncounter(bo, debug=False, fast=False):
    solutions = []
    solve(bo, sols=solutions, fast=fast)

    if debug:
        if len(solutions) == 1:
            print("There was a unique solution!")
        elif len(solutions) == 0:
            print("There was no solution!")
        else:
            print(f"\nThere were {len(solutions)} solutions")

        for solu in solutions:
            print("\n")
            print(np.matrix(solu))

    return solutions


def solve(bo, sols=None, fast=False):
    sleeptimer = sleeptime
    if fast:
        sleeptimer = 0

    global currGrid
    currGrid = bo

    for row in range(0, basesize**2):
        for col in range(0, basesize**2):
            # Find empty field
            if bo[row][col] == 0:
                for n in range(1, basesize**2+1):
                    if check(n, row, col, bo):
                        bo[row][col] = n
                        # if showSteps:
                        sleep(sleeptimer)
                        solve(bo, sols)
                        bo[row][col] = 0
                return

    # print(np.matrix(bo))
    sols.append(copy.deepcopy(bo))


def isSolved(bo):
    for row in range(basesize**2):
        for col in range(basesize**2):
            if bo[row][col] == 0:
                return False
    return True


def gen(grid, seed=None):
    if seed == None:
        seed = random.randint(1, 100000000000000000000)

    for i in range(0, basesize**4):
        row = i//(basesize**2)
        col = i % (basesize**2)
        if grid[row][col] == 0:
            random.seed(a=seed+575+67*i)
            random.shuffle(possibleNumbers)
            for num in possibleNumbers:
                if check(num, row, col, grid):
                    grid[row][col] = num
                    if isSolved(grid):
                        return True
                    elif gen(grid, seed+10):
                        return True
            break
    grid[row][col] = 0


def removeFields(grid, count=15, seed=None):
    if seed == None:
        seed = random.randint(1, 100000000000000000000)
    for i in range(0, count):
        print(f"Cycle {i+1}")

        random.seed(a=seed+175+57*i)
        row = random.randint(0, basesize**2-1)
        random.seed(a=seed+695+13*i)
        col = random.randint(0, basesize**2-1)
        if grid[row][col] != 0:
            backup = grid[row][col]
            grid[row][col] = 0
            # print(grid)

            gridCopy = copy.deepcopy(grid)
            if len(solutioncounter(gridCopy, fast=True)) != 1:
                grid[row][col] = backup
                print("Used backup")


def generateSudoku(seed=None, count=35, baseSize=3, debug=False):
    grid = [[0 for i in range(basesize**2)]for j in range(basesize**2)]
    gen(grid, seed=seed)
    removeFields(grid, count=count, seed=seed)
    return grid


# exp = generateSudoku(count=250)
# print(np.matrix(exp))
# solutioncounter(exp,debug=True)
