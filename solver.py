import math


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


# Checking if it is possible to put a number at a certain point.
def check(num, row, col, bo):
    # Check Row
    if num in bo[row]:
        return False
    # Check Col
    for i in range(0, (basesize ** 2) - 1):
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
    for i in range(0, basesize-1):
        rows.append(squarerow*basesize + i)
        cols.append(squarecol*basesize + i)

    for roww in rows:
        for coll in cols:
            if bo[roww][coll] == num:
                return False
    return True
