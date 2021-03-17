import time
from config import activeConfig as c

stepcount = 0
timetosleep = 0

bfsCont = True

class EntryData:
    def __init__(self, row, col, choices, choicesList = []):
        self.row = row
        self.col = col
        self.choices = choices
        self.choicesList = choicesList
    
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


def backtrackNew(matrix):
    global bfsCont, stepcount
    stepcount = 0
    bfsCont = True
    solveSudokuBacktrackHelper(matrix)
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
        for j in range(c * 3, c * 3 + 3):
            if (row != i or col != j) and matrix[i][j] != 0 and matrix[i][j] == matrix[row][col]:
                return False
    return True

def findEmpty(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                # numChoices, choicesList = countChoices(matrix, i, j)
                
                return EntryData(i, j, 1)
                # if currCandidate.choices > numChoices:
                #     currCandidate.setData(i, j, numChoices, choicesList)
    return EntryData(-1, -1, 100)



def solveSudokuBacktrackHelper(matrix):

    global bfsCont, stepcount
    stepcount += 1
    if not bfsCont:
        return
    
    # bCandidate = EntryData(-1, -1, 100)
    # for i in range(9):
    #     for j in range(9):
    #         if matrix[i][j] == 0:
    #             numChoices, choicesList = countChoices(matrix, i, j)
    #             if currCandidate.choices > numChoices:
    #                 currCandidate.setData(i, j, numChoices, choicesList)
    currCandidate = findEmpty(matrix)
    
    if currCandidate.choices == 100:
        
        bfsCont = False
        return
    row = currCandidate.row
    col = currCandidate.col

    for j in range(1,10):
    # for j in currCandidate.choicesList:


        if not bfsCont:
            return
        matrix[row][col] = j

        time.sleep(c.sleeptime)
        if canBeCorrect(matrix, row, col):
            solveSudokuBacktrackHelper(matrix)
    if not bfsCont:
        
        return
    matrix[row][col] = 0
    time.sleep(timetosleep)




if __name__ == "__main__":
    testgrid = [[3, 4, 0, 0, 1, 0, 9, 0, 0], [0, 0, 1, 0, 0, 4, 0, 8, 3], [5, 0, 0, 0, 0, 0, 0, 1, 0], [9, 1, 0, 0, 5, 0, 0, 0, 0], [0, 6, 4, 0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 8, 0, 0, 4, 9], [0, 8, 0, 0, 0, 0, 0, 0, 2], [2, 3, 0, 9, 0, 0, 4, 0, 0], [0, 0, 9, 0, 4, 0, 0, 5, 8]]
    backtrackNew(testgrid)
    print(testgrid)