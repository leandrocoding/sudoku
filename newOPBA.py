import time


stepcount = 0
timetosleep = 0.1

bfsCont = True

class EntryData:
    def __init__(self, row, col, choices):
        self.row = row
        self.col = col
        self.choices = choices
    
    def setData(self, row, col, choices, choicesList = []):
        self.row = row
        self.col = col
        self.choices = choices
        self.choicesList = choicesList


def countChoices(matrix, i, j):
    """Gives the possible Numbers at a position on a sudoku grid. """
    canPick = [True for _ in range(10)]
    # canPick[0] = False

    for k in range(9):
        canPick[matrix[i][k]] = False
    for k in range(9):
        canPick[matrix[k][j]] = False

    r = i//3
    c = j//3
    for row in range(r*3,(r+1)*3):
        for col in range(c*3,(c+1)*3):
            canPick[matrix[row][col]] = False

    count = 0
    outlist = []
    for k in range(1,10):
        if canPick[k]:
            count+=1
            outlist.append(k)
    # print(outlist)
    return count, outlist
    # out=[]
    # for num, value in enumerate(canPick):
    #     if value:
    #         out.append(num)
    # return out


def bfs(matrix):
    global bfsCont, stepcount
    stepcount = 0
    bfsCont = True
    solveSudokuBFSHelper(matrix)
    print(stepcount)

def canBeCorrect(matrix, row, col):

    # Check Row
    for c in range(9):
        if matrix[row][col] != 0 and col != c and matrix[row][col] == matrix[row][c]:
            return False
    # Check Col
    for r in range(9):
        if matrix[row][col] != 0 and row != r and matrix[row][col] == matrix[r][col]:
            return False
    
    # Check Squares
    r = row // 3
    c = col // 3
    for i in range(r * 3, r * 3 + 3):
        for j in range(c * 3, c * 3 + 1):
            if (row != i or col != j) and matrix[i][j] != 0 and matrix[i][j] == matrix[row][col]:
                return False
    return True


def solveSudokuBFSHelper(matrix):

    global bfsCont, stepcount
    if not bfsCont:
        return
    
    bestCandidate = EntryData(-1, -1, 100)
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                numChoices, choicesList = countChoices(matrix, i, j)
                if bestCandidate.choices > numChoices:
                    bestCandidate.setData(i, j, numChoices, choicesList)
    
    if bestCandidate.choices == 100:
        
        bfsCont = False
        return
    row = bestCandidate.row
    col = bestCandidate.col

    # for j in range(1,10):
    for j in bestCandidate.choicesList:


        if not bfsCont:
            return
        matrix[row][col] = j

        time.sleep(timetosleep)
        if canBeCorrect(matrix, row, col):
            solveSudokuBFSHelper(matrix)
    if not bfsCont:
        
        return
    matrix[row][col] = 0
    time.sleep(timetosleep)




if __name__ == "__main__":
    testgrid = [[3, 4, 0, 0, 1, 0, 9, 0, 0], [0, 0, 1, 0, 0, 4, 0, 8, 3], [5, 0, 0, 0, 0, 0, 0, 1, 0], [9, 1, 0, 0, 5, 0, 0, 0, 0], [0, 6, 4, 0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 8, 0, 0, 4, 9], [0, 8, 0, 0, 0, 0, 0, 0, 2], [2, 3, 0, 9, 0, 0, 4, 0, 0], [0, 0, 9, 0, 4, 0, 0, 5, 8]]
    bfs(testgrid)
    print(testgrid)