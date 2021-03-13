import time
from config import activeConfig as con

DLCont = True
timetosleep = 0.1
stepcount = 0
class DLHeaderNode:
    def __init__(self, up, down, left, right, size):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.size = size
    

class DLNode:
    def __init__(self, up, down, left, right, header, rowNumber):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.header = header
        self.rowNumber = rowNumber



def dancingLinks(matrix):
    numRows = 729
    numCols = 324
    masterNode = DLHeaderNode(None, None, None, None, -1)
    topColumnNodeList = []
    topRowNodeList = []

    prevCol = masterNode
    for c in range(numCols):
        currentCol = DLHeaderNode(None, None, prevCol, None, 0)
        topColumnNodeList.append(currentCol)
        prevCol.right = currentCol
        prevCol = currentCol
    
    topColumnNodeList[len(topColumnNodeList)-1].right = masterNode
    masterNode.left = topColumnNodeList[len(topColumnNodeList)-1]

    for i in range(numRows):
        r = i // 81
        c = (i%81)//9
        num = i % 9 + 1

    
        node1Index = r*9 + c
        node2Index = 80 + 9*r + num
        node3Index = 161 + 9*c + num
        b = (r//3)*3 + c//3 
        node4Index = 242 + 9*b + num

        node1 = DLNode(None, None, None, None, topColumnNodeList[node1Index], i)
        node2 = DLNode(None, None, node1, None, topColumnNodeList[node2Index], i)
        node3 = DLNode(None, None, node2, None, topColumnNodeList[node3Index], i)
        node4 = DLNode(None, None, node3, None, topColumnNodeList[node4Index], i)

        node1.right = node2
        node2.right = node3
        node3.right = node4

        topRowNodeList.append(node1)

        node4.right = node1
        node1.left = node4

        topCol1 = topColumnNodeList[node1Index]
        topCol2 = topColumnNodeList[node2Index]
        topCol3 = topColumnNodeList[node3Index]
        topCol4 = topColumnNodeList[node4Index]

        addNodeToBottomOfAColumn(node1, topCol1)
        addNodeToBottomOfAColumn(node2, topCol2)
        addNodeToBottomOfAColumn(node3, topCol3)
        addNodeToBottomOfAColumn(node4, topCol4)


        topColumnNodeList[node1Index].size +=1
        topColumnNodeList[node2Index].size +=1
        topColumnNodeList[node3Index].size +=1
        topColumnNodeList[node4Index].size +=1



    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=0:
                num = matrix[i][j]
                rowNumber = (num-1) + i*81 +j*9

                headNodeFromARow = topRowNodeList[rowNumber]
                coverColumn(headNodeFromARow.header)
                temp = headNodeFromARow.right
                while temp != headNodeFromARow:
                    coverColumn(temp.header)
                    temp = temp.right

    global DLCont
    DLCont = True

    DLSearch(0, masterNode, matrix)



def DLSearch(k, masterNode, matrix):
    global DLCont, stepcount
    if not DLCont:
        return
    
    if masterNode.right == masterNode:
        DLCont = False
        print(stepcount)
        return
    
    tempC = masterNode.right
    c = tempC
    while tempC != masterNode:
        if c.size > tempC.size:
            c = tempC
        tempC = tempC.right
    coverColumn(c)

    r = c.down

    while r != c:
        if not DLCont:
            return
        
        correspondingSudokuBoardRow = r.rowNumber //81
        correspondingSudokuBoardColumn = (r.rowNumber%81)//9
        correspondingSudokuBoardNumber = r.rowNumber % 9 +1
        stepcount += 1
        matrix[correspondingSudokuBoardRow][correspondingSudokuBoardColumn] = correspondingSudokuBoardNumber
        time.sleep(con.sleeptime)
        # row = correspondingSudokuBoardRow
        # col = correspondingSudokuBoardColumn
        # i = correspondingSudokuBoardNumber

        j = r.right
        while j != r:
            coverColumn(j.header)
            j = j.right
        
        DLSearch(k+1, masterNode, matrix)

        if not DLCont:
            return

        matrix[correspondingSudokuBoardRow][correspondingSudokuBoardColumn] = 0

        j = r.left
        while j != r:
            uncoverColumn(j.header)
            j = j.left
        
        r = r.down
    
    uncoverColumn(c)


def addNodeToBottomOfAColumn(nodeToAdd, columnTop):
    temp = columnTop
    while temp.down is not None and temp.down != columnTop:
        temp = temp.down
    temp.down = nodeToAdd
    nodeToAdd.up = temp

    nodeToAdd.down = columnTop
    columnTop.up = nodeToAdd


def coverColumn(topColumnNode):
    c = topColumnNode

    c.right.left = c.left
    c.left.right = c.right

    i = c.down
    while i!= c:
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down

            j.header.size -=1
            j = j.right
        i = i.down


def uncoverColumn(topColumnNode):
    c = topColumnNode

    i = c.up
    while i != c:
        j = i.left
        while j != i:
            j.header.size +=1

            j.down.up = j
            j.up.down = j

            j = j.K_LEFT

        i = i.up

    c.right.left = c
    c.left.right = c



if __name__ == "__main__":
    testgrid = [[3, 4, 0, 0, 1, 0, 9, 0, 0], [0, 0, 1, 0, 0, 4, 0, 8, 3], [5, 0, 0, 0, 0, 0, 0, 1, 0], [9, 1, 0, 0, 5, 0, 0, 0, 0], [0, 6, 4, 0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 8, 0, 0, 4, 9], [0, 8, 0, 0, 0, 0, 0, 0, 2], [2, 3, 0, 9, 0, 0, 4, 0, 0], [0, 0, 9, 0, 4, 0, 0, 5, 8]]
    dancingLinks(testgrid)
    print(testgrid)