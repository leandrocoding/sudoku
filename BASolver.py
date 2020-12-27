import math
import random
import copy
import inspect
import ujson
from time import sleep
from config import Config as c,Temp as t

"""
Dimensions of the board variable?
By default it should be 9x9
The field can be bigger it however has to follow the rule, that the inner field is allways the squareroot tall and wide of the whole field.
Example:
Normal sudoku inner Fileds: 3x3, outer field is made out of 3x3 of the inner fields
smaller Sudoku: inner field made out of 2X2 outer field is made of 2x2 of the outer field
large Sudoku: inner field 4x4 outer field 16x16 or made out of 4x4 of the inner field.


A board is defined as Colloms in Rows.   x=col y=row cords are in the format bo [row][col] or bo[y][x]
A "0" stands dor empty.
"""
t.possibleNumbers = []
for i in range(c.basesize**2+1):
    t.possibleNumbers.append(i)


# Checking if it is possible to put a number at a certain point.


def check(num, row, col, bo):
    """Checks if it is possible to put a number at a certain point. (LEGACY)"""
    # Check Row
    for i in range(9):
        if bo[i][col] ==num or bo[row][i] == num:
            return False
    return checksquare(num,row,col,bo)


    # if num in bo[row]:
    #     return False
    # # Check Col
    # for i in range(0, (c.basesize ** 2)):
    #     if num == bo[i][col]:
    #         return False
    # # Check Square
    # return checksquare(num, row, col, bo)

    # return True


def checksquare(num, row, col, bo):
    squarerow = math.floor(row/c.basesize)
    squarecol = math.floor(col/c.basesize)
    for rown in range(3):
        for coln in range(3):
            if bo[squarerow*3 + rown][col] == num:
                return False
            if bo[row][squarecol*3 + coln] == num:
                return False
    return True
    # rows = []
    # cols = []
    # for i in range(0, c.basesize):
    #     rows.append(squarerow*c.basesize + i)
    #     cols.append(squarecol*c.basesize + i)

    # for roww in rows:
    #     for coll in cols:
    #         if bo[roww][coll] == num:
    #             return False
    # return True


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
            print(solu)

    return solutions


def solve(bo, sols=None, fast=False):
    # sleeptimer = c.sleeptime
    sleeptimer=0
    # if fast:
    #     sleeptimer=0
    global currGrid
    currGrid = bo

    for row in range(0, c.basesize**2):
        for col in range(0, c.basesize**2):
            # Find empty field
            if bo[row][col] == 0:
                for n in range(1, c.basesize**2+1):
                    if check(n, row, col, bo):
                        bo[row][col] = n
                        # if showSteps:
                        # sleep(sleeptimer)
                        solve(bo, sols)
                        bo[row][col] = 0
                return

    # print(np.matrix(bo))
    sols.append(ujson.loads(ujson.dumps(bo)))


def isSolved(bo):
    for row in range(c.basesize**2):
        for col in range(c.basesize**2):
            if bo[row][col] == 0:
                return False
    return True


def gen(grid, seed=None):
    if seed is None:
        seed = random.randint(1, 100000000000000000000)

    for i in range(0, c.basesize**4):
        row = i//(c.basesize**2)
        col = i % (c.basesize**2)
        if grid[row][col] == 0:
            random.seed(a=seed+575+67*i)
            random.shuffle(c.possibleNumbers)
            for num in c.possibleNumbers:
                if check(num, row, col, grid):
                    grid[row][col] = num
                    if isSolved(grid):
                        return True
                    elif gen(grid, seed+10):
                        return True
            break
    grid[row][col] = 0


def removeFields(grid, count=15, seed=None):
    if seed is None:
        seed = random.randint(1, 100000000000000000000)
    for i in range(0, count):
        print(f"Cycle {i+1}")

        random.seed(a=seed+175+57*i)
        row = random.randint(0, c.basesize**2-1)
        random.seed(a=seed+695+13*i)
        col = random.randint(0, c.basesize**2-1)
        if grid[row][col] != 0:
            backup = grid[row][col]
            grid[row][col] = 0
            # print(grid)

            gridCopy = copy.deepcopy(grid)
            if len(solutioncounter(gridCopy, fast=True)) != 1:
                grid[row][col] = backup
                print("Used backup")


def generateSudoku(seed=None, count=35, debug=False):
    grid = [[0 for i in range(c.basesize**2)]for j in range(c.basesize**2)]
    gen(grid, seed=seed)
    removeFields(grid, count=count, seed=seed)
    return grid



if __name__ == "__main__":
    solve()