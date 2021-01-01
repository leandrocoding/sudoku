class InvaldSudoku(Exception):
    pass

class NoNSolvable(Exception):
    pass
def checksquare(num, i, j, grid):
    squarerow = i//3
    squarecol = j//3
    for rown in range(3):
        for coln in range(3):
            if grid[int(squarerow*3) + rown][j] == num:
                return False
            if grid[i][int(squarecol*3) + coln] == num:
                return False
    return True


def check(num, i, j, grid):
    for k in range(9):
        if grid[k][j] == num or grid[i][k] == num:
            return False
    return checksquare(num, i, j, grid)


def bASolve(grid):
    for i in range(9):
        for j in range(9):
            number = grid[i][j]
            if number == 0:
                for n in range(1, 10):
                    if(check(n, i, j, grid)):
                        grid[i][j] = n
                        if bASolve(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def bASolverHandle(grid):
    if any([not num<10 for row in grid for num in row]):
        raise NoNSolvable("Sudoku could not be solved")
    if len(grid)!=9 or len(grid[0])!=9:
        raise InvaldSudoku("Sudoku is not Valid, it has to be 9x9")
        return False
    bASolve(grid)
    
    if any([not 0<num<10 for row in grid for num in row]):
        raise NoNSolvable("Sudoku could not be solved")

    return grid


    


if __name__ == "__main__":
    pass
