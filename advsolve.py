from config import Config as c, Temp as t
from solver import check
from time import sleep
import copy

t.possibls=[]
# Format [[[1,3,6],1],[4,1,6],[9,1],[0],[0],[5,9,1,4],[0],[0],[0]],[[5,6,7],[0],[1]]
# Format = [[[[[1,5,8],0],[[6,1,6],1]....]]]
# Format get length of Data poss[row][col][0].length()

def rowcoltoNum(row,col):
    return row*c.basesize**2+col
def getLen(elem):
    leng=len(elem[0])
    if leng!=0:
        return leng
    return 99

def numtoRowCol(num):
    row=num//c.basesize**2
    col=num % c.basesize**2
    return (row,col)

# row,col = numtoRowCol(15)
# print(f"Row: {row} \n Col: {col}")
# print(rowcoltoNum(row,col))



def findPossi(bo):
    t.possibls=[]
    for row,rowVal in enumerate(bo):
        for col,colVal in enumerate(rowVal):
            localpossi=[]
            # localindicator=[]
            for n in range(1,c.basesize**2+1):
                if colVal==0:
                    # print(bo[row][col])

                    if check(n,row,col,bo):
                        localpossi.append(n)
                        
      
            # localindicator.append([localpossi,rowcoltoNum(row,col)])
            if bo[row][col]==0:
                t.possibls.append(copy.deepcopy([localpossi,rowcoltoNum(row,col)]))

    if t.possibls:
        return True
    else:
        return False
                


    t.possibls.sort(key=getLen)
    # for elem in t.possibls:
    #     if len(elem[0])==0:


    return t.possibls



def solcountadv(bo):
    sols=[]
    solveadv(bo,sols)

def solveadv(bo,sols=None):
    
    solve(bo,sols)

    
def solve(bo,sols=None):
    sleeptimer = c.sleeptime
    # if fast:
    #     sleeptimer=0
    # global currGrid
    # currGrid = bo
    
    # for poss in possis:
    #     if poss
    # poss[]
    findPossi(bo)
    posib=t.possibls
    
    for posi in posib:
        ns=posi[0]
        row,col = numtoRowCol(posi[1])
        for n in ns:

            if check(n, row, col, bo):
                bo[row][col] = n
                sleep(sleeptimer)
                
                
                solveadv(bo, sols)
                bo[row][col] = 0
        return True
        # for n in ns:
        #     bo[row][col] = n
        #     solveadv(bo, sols)
        #     bo[row][col] = 0
            
                        

    # print(np.matrix(bo))
    sols.append(copy.deepcopy(bo))










# def sortbyPossibilities:



# class Field:
#     posibil=[]
#     row=0
#     col=0
#     grid=[]

#     possibilcount=0

#     def __init__(self,row,col,bo)

#     def getNumPos(self):
#         self.possibilcount=self.posibil
    
#     def checkpos(bo,row,col):
#         ret=[(row,col)]
#         for num in range(1,c.basesize**2+1):
#             if check(num, row, col, bo):
#                 ret.append(num)
#         return ret

# class Board:
#     grid=[]
#     possis=[]

#     def __init__(self,bo):
#         self.grid=bo
#         self.checkboard(self.grid)
        

#     def checkboard(bo):
#         for row in range(c.basesize**2):
#             for col in range(c.basesize**2):
#                 self.possis.append()

                

# def fieldInit():
    

# def solve(bo):
#     pass


    # pass

# possibis=[[[0],[0],[0]]]

