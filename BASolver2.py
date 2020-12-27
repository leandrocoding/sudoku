

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


if __name__ == "__main__":
    gr = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    bASolve(gr)
    print(gr)