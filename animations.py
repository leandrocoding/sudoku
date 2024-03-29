"""LEGACY GUI application. This was used to make illustrations for the Matura Project.

Basic and advanced Backtracking is Implemented."""


import pygame
import sys
from multiprocessing.pool import ThreadPool



from newBA import backtrackNew as backNew
from newDancesolver import dancingLinks
from config import activeConfig as c, Temp as t, Solvertype
# from OPBASolver import solveadv
from newOPBA import bfs
import XSolver
import makesud



# ***************Testing Config****************
# from testGrids import Grids
# t.currGrid = copy.deepcopy(Grids.grid9x9_1)
# t.currGrid = XSolver.exact_to_matrix(9, makesud.make_sudoku())


t.currGrid = [[3, 4, 0, 0, 1, 0, 9, 0, 0], [0, 0, 1, 0, 0, 4, 0, 8, 3], [5, 0, 0, 0, 0, 0, 0, 1, 0], [9, 1, 0, 0, 5, 0, 0, 0, 0], [0, 6, 4, 0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 8, 0, 0, 4, 9], [0, 8, 0, 0, 0, 0, 0, 0, 2], [2, 3, 0, 9, 0, 0, 4, 0, 0], [0, 0, 9, 0, 4, 0, 0, 5, 8]]
# print(t.currGrid)

drawingselector = True
# ****************End of Config****************

def run():
    setup()
    mainloop()


def mainloop():

    while t.pygameActive:
        for event in pygame.event.get():
            eventHandler(event)
        draw(t.currGrid)
    pygame.quit()


def resetGrid():
    # t.currGrid = XSolver.exact_to_matrix(9, makesud.make_sudoku())
    t.currGrid = [[3, 4, 0, 0, 1, 0, 9, 0, 0], [0, 0, 1, 0, 0, 4, 0, 8, 3], [5, 0, 0, 0, 0, 0, 0, 1, 0], [9, 1, 0, 0, 5, 0, 0, 0, 0], [0, 6, 4, 0, 0, 0, 1, 3, 0], [0, 0, 0, 0, 8, 0, 0, 4, 9], [0, 8, 0, 0, 0, 0, 0, 0, 2], [2, 3, 0, 9, 0, 0, 4, 0, 0], [0, 0, 9, 0, 4, 0, 0, 5, 8]]

    # print(findPossi(t.currGrid))

def setup():
    global root, font, running
    pygame.init()
    t.pygameActive=True

    pygame.display.set_caption("Sudoku")


    root = pygame.display.set_mode(
        (c.resolutionField, c.resolutionField+c.spacebelowinPX))

    root.fill((250, 250, 250))

    font = pygame.font.SysFont(None, c.resolutionField//c.basesize**2)
    t.selector_pos = [0, 0]  # (Row,Col)
    t.given = []
    running = True
    t.pygameActive=True
    # setupconfig()


def setConfig(basesize=3, resolutionField=900, spacebelowinPX=100, displayinHexa=False, sleeptime=0):
    c.basesize=basesize
    c.resolutionField=resolutionField
    c.spacebelowinPX=spacebelowinPX
    c.displayinHexa=displayinHexa
    c.sleeptime=sleeptime

    return c


def draw_field():
    for i in range(c.basesize**2+1):
        pygame.draw.line(root, (0, 0, 0), (i*c.resolutionField//(c.basesize**2), 0),
                         (i*c.resolutionField//(c.basesize**2), c.resolutionField), 2)
        pygame.draw.line(root, (0, 0, 0), (0, i*c.resolutionField//(c.basesize**2)),
                         (c.resolutionField, i*c.resolutionField//(c.basesize**2)), 2)

    for i in range(c.basesize+1):
        pygame.draw.line(root, (0, 0, 0), (0, i*c.resolutionField//(c.basesize)),
                         (c.resolutionField, i*c.resolutionField//(c.basesize)), 5)
        pygame.draw.line(root, (0, 0, 0), (i*c.resolutionField//(c.basesize), 0),
                         (i*c.resolutionField//(c.basesize), c.resolutionField), 5)


def draw_num(grid):
    if len(grid) != c.basesize**2:
        print(
            f"Expected Sudoku with side length {c.basesize**2}. Instead got a Sudoku with a side length of {len(grid)}")
        print("Please check your config!")
        print("Exiting now!")
        global running
        running = False
        pygame.quit()
        sys.exit()
        return False

    for row in range(0, c.basesize**2):
        for col in range(0, c.basesize**2):
            num = grid[row][col]
            if num != 0:
                if c.displayinHexa:
                    num = hex(num).split('x')[-1]
                text = font.render(str(num), True, (0, 0, 0), (250, 250, 250))
                textRe = text.get_rect()
                textRect = textRe.move((row*c.resolutionField//(c.basesize**2)+(int(c.resolutionField/(
                    c.basesize**3*1.1))), (col*c.resolutionField//(c.basesize**2)+(c.resolutionField//(c.basesize**3*2)))))
                root.blit(text, textRect)


def draw_footer():
    pygame.draw.line(root, (0, 0, 0), (0, c.resolutionField),
                     (c.resolutionField, c.resolutionField), 10)
    text = font.render(Solvertype.solvers[c.currsolverindex], True, (0, 0, 0), (250, 250, 250))
    textRe = text.get_rect()
    textRect = textRe.move((0,c.resolutionField+round(c.spacebelowinPX/3)))
    root.blit(text, textRect)
    



def draw_selector():
    row = t.selector_pos[0]
    col = t.selector_pos[1]
    selRect = pygame.Rect(col*c.resolutionField//c.basesize**2, row*c.resolutionField//c.basesize**2,
                          c.resolutionField//c.basesize**2, c.resolutionField//c.basesize**2)
    pygame.draw.rect(root, (200, 0, 0), selRect, 5)


def draw(grid):
    root.fill((250, 250, 250))
    draw_field()
    draw_num(grid)
    draw_footer()
    if drawingselector:

        draw_selector()
    pygame.display.update()


def move_selector(row_delta, col_delta):
    row_old = t.selector_pos[0]
    col_old = t.selector_pos[1]

    if(0 <= row_old-row_delta < c.basesize**2):
        t.selector_pos[0] = row_old-row_delta
    if(0 <= col_old+col_delta < c.basesize**2):
        t.selector_pos[1] = col_old+col_delta


def setSelector(row, col):
    t.selector_pos[0] = int(row)
    t.selector_pos[1] = int(col)

def changeselected(tonum):
    t.currGrid[t.selector_pos[1]][t.selector_pos[0]] = tonum


def mouseSelect():
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    if y_mouse > c.resolutionField-5 or x_mouse > c.resolutionField-5:
        return

    col = x_mouse//(c.resolutionField//c.basesize**2)
    row = y_mouse//(c.resolutionField//c.basesize**2)
    setSelector(row, col)


def givenChecker(grid):
    global given
    given = []
    for ro, row in enumerate(grid):
        for co, col in enumerate(row):
            if col != 0:
                given.append((ro, co))


# def guiSolve(bo):
#     solutions = []
#     # solve(t.currGrid, sols=solutions)
#     solveadv(t.currGrid, sols=solutions)

#     bo = solutions[0]
#     print("Solved")
#     print(bo)

#     if len(solutions) == 0:
#         print("There was no solution!")
#         return bo
#     return solutions[0]


def setCurrGrid(ret):
    # global currGrid
    # t.currGrid = ret
    pass

def solveselect(curr,abc=None):
    c.solver=Solvertype.solvers[c.currsolverindex]
    if c.solver==Solvertype.backnorm:
        # return solve(curr,abc)
        return backNew(curr)

    elif c.solver==Solvertype.backadv:
        # return solveadv(curr,abc)
        return bfs(curr)
    elif c.solver==Solvertype.dancinglinks:
        # return solveadv(curr,abc)
        return dancingLinks(curr)
    else:
        print("Not implemented at the Moment. \n Coming soon!")
        return t.currGrid



def solveThread(curr):

    pool = ThreadPool(processes=1)

    _ = pool.apply_async(
        solveselect, (curr,c), callback=setCurrGrid)

def changeSolver(dir):
    newindex= c.currsolverindex+dir
    if newindex>len(Solvertype.solvers)-1:
        newindex+=-len(Solvertype.solvers)
    if newindex<0:
        newindex+=len(Solvertype.solvers)
    c.currsolverindex=newindex

# Eventhandling



def modifysleeptime(dirr):
    newtime = c.sleeptime + dirr
    if newtime>=0:
        c.sleeptime = newtime
    else:
        c.sleeptime = 0
    pygame.display.set_caption(f"Sudoku  Sleeptime: {c.sleeptime:.2f}s")


def toggledrawingselector():
    global drawingselector
    drawingselector = not drawingselector

def eventHandler(event):
    if event.type == pygame.QUIT:
        global running
        running = False
        t.pygameActive=False
        pygame.quit()
        sys.exit()
    controlls(event)


def controlls(event):
    if event.type == pygame.KEYDOWN:

        # Move Selector
        if event.key == pygame.K_UP:
            move_selector(1, 0)
        if event.key == pygame.K_DOWN:
            move_selector(-1, 0)
        if event.key == pygame.K_RIGHT:
            move_selector(0, 1)
        if event.key == pygame.K_LEFT:
            move_selector(0, -1)
        if event.key == pygame.K_m:
            # start_new_thread(confguirun,())
            # t1 = threading.Thread(target=confguirun)

            # t1.start()
            pass
        if event.key == pygame.K_r:
            resetGrid()
        if event.key == pygame.K_LCTRL:
            changeSolver(-1)
        if event.key == pygame.K_LSHIFT:
            changeSolver(1)
        if event.key == pygame.K_COMMA:
            modifysleeptime(-0.02)
        if event.key == pygame.K_PERIOD:
            modifysleeptime(0.02)
            
        if event.key == pygame.K_u:
            toggledrawingselector()
        # Output current grid in console
        if event.key == pygame.K_p:
            print(t.currGrid)
        if event.key == pygame.K_i:
            print("Saving to disk")
            pygame.image.save(root, f"Image 111.png")



        #     pooll = ThreadPool(processes=1)

        # _ = pooll.apply_async(confguirun, ())


        # Num input
        # TODO Input for numbers
        if event.key == pygame.K_1:
            changeselected(1)
        if event.key == pygame.K_2:
            changeselected(2)
        if event.key == pygame.K_3:
            changeselected(3)
        if event.key == pygame.K_4:
            changeselected(4)
        if event.key == pygame.K_5:
            changeselected(5)
        if event.key == pygame.K_6:
            changeselected(6)
        if event.key == pygame.K_7:
            changeselected(7)
        if event.key == pygame.K_8:
            changeselected(8)
        if event.key == pygame.K_9:
            changeselected(9)
        if event.key == pygame.K_DELETE or event.key == pygame.K_0:
            changeselected(0)
        

        #

        if event.key == pygame.K_s:
            solveThread(t.currGrid)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseSelect()




if __name__ == "__main__":
    run()
