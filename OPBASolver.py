from config import Config as c, Temp as t
from BASolver2 import check
from time import sleep
import ujson
import copy

t.possibls=[]

def rowcoltoNum(row,col):
    return row*c.basesize**2+col
def getLen(elem):

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
    t.possibls=[]
    for row,rowVal in enumerate(bo):
        for col,colVal in enumerate(rowVal):
            localpossi=newPossiFinder(bo, col, row)

            if bo[row][col]==0:
                # Here ujson.loads(ujson.dumps()) is used because it is much faster than copy.deepcopy() to make a copy of a list.
                t.possibls.append(ujson.loads(ujson.dumps([localpossi,rowcoltoNum(row,col)])))
    t.possibls.sort(key=getLen)
    if t.possibls:
        return True
    else:
        return False

    return t.possibls

def solcountadv(bo):
    """Returns all Solutions"""
    sols=[]
    solveadv(bo,sols)
    return sols

def solveadv(bo,sols=None):

    solve(bo,sols)


def solve(bo,sols=None):
    """Solve Sudoku with Optimized Backtracking algorithm"""
    sleeptimer = c.sleeptime

    findPossi(bo)

    posib=t.possibls

    for posi in posib:
        ns=posi[0]
        row,col = numtoRowCol(posi[1])
        for n in ns:

            if check(n, row, col, bo):
                bo[row][col] = n
                sleep(sleeptimer)


                solve(bo, sols)
                bo[row][col] = 0
        return True

    # Here ujson.loads(ujson.dumps()) is used because it is much faster than copy.deepcopy() to make a copy of a list.
    sols.append(ujson.loads(ujson.dumps(bo)))
