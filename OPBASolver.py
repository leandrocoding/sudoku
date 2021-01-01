from config import Config as c, Temp as t
from BASolver2 import check
from time import sleep
import ujson
import copy
class InvaldSudoku(Exception):
    pass

class NoNSolvable(Exception):
    pass
t.possibls=[]

def OPSolverHandle(grid):
    if any([not num<10 for row in grid for num in row]):
        raise InvaldSudoku("Sudoku has value bigger than 9 ")
    if len(grid)!=9 or len(grid[0])!=9:
        raise InvaldSudoku("Sudoku is not Valid, it has to be 9x9")
        return False
    sols = []
    solve(grid, sols)
    grid = sols[0]
    
    if any([not 0<num<10 for row in grid for num in row]):
        raise NoNSolvable("Sudoku could not be solved")

    return grid
def rowcoltoNum(row,col):
    """Converts 2D cooridinate to a 1D coordinate"""
    return row*c.basesize**2+col
def getLen(elem):
    """This function is used to Sort the fileds by possibilities."""
    leng=len(elem[0])
    if leng!=0:
        return leng
    return 99

def numtoRowCol(num):
    """"Convert number to row col"""
    row=num//c.basesize**2
    col=num % c.basesize**2
    return (row,col)

def newPossiFinder(bo,i,j):
    """Gives the possible Numbers at a position on a sudoku grid. """
    pickable = [True for _ in range(10)]
    pickable[0] = False

    for k in range(9):
        pickable[bo[i][k]] = False
    for k in range(9):
        pickable[bo[k][i]] = False

    r = j//3
    c = i//3
    for row in range(r*3,(r+1)*3):
        for col in range(c*3,(c+1)*3):
            pickable[bo[row][col]] = False
    out=[]
    for num, value in enumerate(pickable):
        if value:
            out.append(num)
    return out


def findPossi(bo):
    """ Find all possibilities for all fields and add them to a list."""
    possis = []
    for row,rowVal in enumerate(bo):
        for col,colVal in enumerate(rowVal):
            localpossi=newPossiFinder(bo, col, row)

            if bo[row][col]==0:
                # Here ujson.loads(ujson.dumps()) is used because it is much faster than copy.deepcopy() to make a copy of a list.
                possis.append(ujson.loads(ujson.dumps([localpossi,rowcoltoNum(row,col)])))
    possis.sort(key=getLen)
    t.possibls = possis
    return possis

def solcountadv(bo):
    """Returns all Solutions"""
    sols=[]
    solveadv(bo,sols)
    return sols

def solveadv(bo,sols=None):

    solve(bo,sols)


def solve(bo,sols=None):
    """Solve Sudoku with Optimized Backtracking algorithm"""

    findPossi(bo)

    posib=t.possibls

    for posi in posib:
        ns=posi[0]
        row,col = numtoRowCol(posi[1])
        for n in ns:

            if check(n, row, col, bo):
                bo[row][col] = n

                if solve(bo, sols):
                    return True
                bo[row][col] = 0
        return True

    # Here ujson.loads(ujson.dumps()) is used because it is much faster than copy.deepcopy() to make a copy of a list.
    sols.append(ujson.loads(ujson.dumps(bo)))
