import pygame
import sys

from solver import solve
from config import Config, Temp
from config import basesize, resolutionField, spacebelowinPX, displayinHexa, showingSteps, currGrid, solving
from testGrids import grid9x9_1, grid16x16_1, grid16x16_2, grid16x16_3, grid16x16_4, grid25x25_1
from multiprocessing.pool import ThreadPool

t = Temp()
# Config
t.currGrid = grid9x9_1

pygame.init()

pygame.display.set_caption("Sudoku")
root = pygame.display.set_mode(
    (resolutionField, resolutionField+spacebelowinPX))

# background = pygame.Surface((900,1000))
# background.fill(pygame.Color("#000000"))
root.fill((250, 250, 250))

font = pygame.font.SysFont(None, resolutionField//basesize**2)
selector_pos = [0, 0]  # (Row,Col)
given = []


def setConfig(basesize=3, resolutionField=900, spacebelowinPX=100, displayinHexa=False, sleeptime=0):
    t.conf = Config(basesize, resolutionField, spacebelowinPX, displayinHexa, sleeptime)
    return t.conf


def draw_field(conf):
    for i in range(conf.basesize**2+1):
        pygame.draw.line(root, (0, 0, 0), (i*conf.resolutionField//(conf.basesize**2), 0),
                         (i*conf.resolutionField//(conf.basesize**2), conf.resolutionField), 2)
        pygame.draw.line(root, (0, 0, 0), (0, i*conf.resolutionField//(conf.basesize**2)),
                         (conf.resolutionField, i*conf.resolutionField//(conf.basesize**2)), 2)

    for i in range(conf.basesize+1):
        pygame.draw.line(root, (0, 0, 0), (0, i*conf.resolutionField//(conf.basesize)),
                         (conf.resolutionField, i*conf.resolutionField//(conf.basesize)), 5)
        pygame.draw.line(root, (0, 0, 0), (i*conf.resolutionField//(conf.basesize), 0),
                         (i*conf.resolutionField//(conf.basesize), conf.resolutionField), 5)


def draw_num(grid,conf):
    if len(grid) != conf.basesize**2:
        print(
            f"Expected Sudoku with side length {conf.basesize**2}. Instead got a Sudoku with a side length of {len(grid)}")
        print("Please check your config!")
        print("Exiting now!")
        global running
        running = False
        pygame.quit()
        sys.exit()

        return False

    for row in range(0, conf.basesize**2):
        for col in range(0, conf.basesize**2):
            num = grid[row][col]
            if num != 0:
                if displayinHexa:
                    num = hex(num).split('x')[-1]
                text = font.render(str(num), True, (0, 0, 0), (250, 250, 250))
                textRe = text.get_rect()
                textRect = textRe.move((row*conf.resolutionField//(conf.basesize**2)+(int(resolutionField/(
                    conf.basesize**3*1.1))), (col*resolutionField//(conf.basesize**2)+(resolutionField//(conf.basesize**3*2)))))
                root.blit(text, textRect)


def draw_footer(conf):
    pygame.draw.line(root, (0, 0, 0), (0, conf.resolutionField),
                     (conf.resolutionField, conf.resolutionField), 10)


def draw_selector(conf):
    row = selector_pos[0]
    col = selector_pos[1]
    selRect = pygame.Rect(col*conf.resolutionField//conf.basesize**2, row*conf.resolutionField //
                          conf.basesize**2, conf.resolutionField//conf.basesize**2, conf.resolutionField//conf.basesize**2)
    pygame.draw.rect(root, (200, 0, 0), selRect, 5)


def draw(grid,conf):
    root.fill((250, 250, 250))
    draw_field(conf)
    draw_num(currGrid,conf)
    draw_footer(conf)
    draw_selector(conf)
    pygame.display.update()


def move_selector(row_delta, col_delta, conf):
    row_old = selector_pos[0]
    col_old = selector_pos[1]

    if(0 <= row_old-row_delta < conf.basesize**2):
        selector_pos[0] = row_old-row_delta
    if(0 <= col_old+col_delta < conf.basesize**2):
        selector_pos[1] = col_old+col_delta


def setSelector(row, col):
    selector_pos[0] = int(row)
    selector_pos[1] = int(col)


def mouseSelect(conf):
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    if y_mouse > conf.resolutionField:
        return
    col = x_mouse//(conf.resolutionField//conf.basesize**2)
    row = y_mouse//(conf.resolutionField//conf.basesize**2)
    setSelector(row, col)


def givenChecker(grid):
    global given
    given = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col != 0:
                given.append((r, c))


def guiSolve(bo,conf):
    # TODO change currGrid to temp.currGrid
    solutions = []
    global currGrid
    solve(currGrid, conf, sols=solutions)
    bo = solutions[0]
    print("Solved")
    print(bo)

    if len(solutions) == 0:
        print("There was no solution!")
        return bo
    return solutions[0]


def setCurrGrid(ret):
    global currGrid
    currGrid = ret


def solveThread(curr,conf):

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     global currGrid

    #     future = executor.submit(guiSolve, currGrid, showingSteps)
    #     newGrid = future.result()

    #     currGrid=newGrid
    #     print(currGrid)

    pool = ThreadPool(processes=1)

    _ = pool.apply_async(
        solve, (curr,conf), callback=setCurrGrid)


# Eventhandling

def eventHandler(event):
    if event.type == pygame.QUIT:
        global running
        running = False
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

        # Num input
        # TODO Input for numbers
        #

        if event.key == pygame.K_s:
            solveThread(currGrid)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseSelect()


running = True

if __name__ == "__main__":
    bs=input("Basesize: ")
    setConfig(basesize=bs)


while running:
    for event in pygame.event.get():
        eventHandler(event)
    draw(currGrid)
