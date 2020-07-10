import pygame
from config import basesize,resolutionField, spacebelowinPX, displayinHexa
import sys
from testGrids import grid9x9_1,grid16x16_1
pygame.init()

pygame.display.set_caption("Sudoku")
root = pygame.display.set_mode((resolutionField, resolutionField+spacebelowinPX))

# background = pygame.Surface((900,1000))
# background.fill(pygame.Color("#000000"))
root.fill((250, 250, 250))
running = True
font = pygame.font.SysFont(None, resolutionField//basesize**2)
selector_pos= [0,0] # (Row,Col)

def draw_field():
    for i in range(basesize**2+1):
        pygame.draw.line(root, (0, 0, 0), (i*resolutionField//(basesize**2), 0), (i*resolutionField//(basesize**2), resolutionField), 2)
        pygame.draw.line(root, (0, 0, 0), (0, i*resolutionField//(basesize**2)), (resolutionField, i*resolutionField//(basesize**2)), 2)

    for i in range(basesize+1):
        pygame.draw.line(root, (0, 0, 0), (0, i*resolutionField//(basesize)), (resolutionField, i*resolutionField//(basesize)), 5)
        pygame.draw.line(root, (0, 0, 0), (i*resolutionField//(basesize), 0), (i*resolutionField//(basesize), resolutionField), 5)


def draw_num(grid):
    if len(grid)!=basesize**2:
        print(f"Expected Sudoku with side length {basesize**2}. Instead got a Sudoku with a side length of {len(grid)}")
        print("Please check your config!")
        print("Exiting now!")
        running = False
        pygame.quit()
        sys.exit()
        
        return False

    for row in range(0,basesize**2):
        for col in range(0,basesize**2):
            num= grid[row][col]
            if num!=0:
                if displayinHexa:
                    num=hex(num).split('x')[-1]
                text = font.render(str(num), True, (0, 0, 0), (250, 250, 250))
                textRe = text.get_rect()
                textRect = textRe.move((row*resolutionField//(basesize**2)+(int(resolutionField/(basesize**3*1.1))), (col*resolutionField//(basesize**2)+(resolutionField//(basesize**3*2)))))
                root.blit(text,textRect)

def draw_footer():
    pygame.draw.line(root, (0, 0, 0), (0, resolutionField), (resolutionField, resolutionField), 10)

def draw_selector():
    row=selector_pos[0]
    col=selector_pos[1]
    selRect=pygame.Rect(col*resolutionField//basesize**2,row*resolutionField//basesize**2,resolutionField//basesize**2,resolutionField//basesize**2)
    pygame.draw.rect(root,(200,0,0),selRect,5)

def move_selector(row_delta,col_delta):
    row_old=selector_pos[0]
    col_old=selector_pos[1]
 
    if(0<=row_old-row_delta<basesize**2):
        selector_pos[0]=row_old-row_delta
    if(0<=col_old+col_delta<basesize**2):
        selector_pos[1]=col_old+col_delta

def setSelector(row,col):
    selector_pos[0]=int(row)
    selector_pos[1]=int(col)

def mouseSelect():
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    if y_mouse>resolutionField:
        return 
    col=x_mouse//(resolutionField//basesize**2)
    row=y_mouse//(resolutionField//basesize**2)
    setSelector(row,col)


# Eventhandling

def eventHandler(event):
    if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()
    controlls(event)

def controlls(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            move_selector(1,0)
        if event.key == pygame.K_DOWN:
            move_selector(-1,0)
        if event.key == pygame.K_RIGHT:
            move_selector(0,1)
        if event.key == pygame.K_LEFT:
            move_selector(0,-1)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseSelect()

    

    






            
        
                    
        


while running:
    for event in pygame.event.get():
        eventHandler(event)
            
    root.fill((250, 250, 250))
    draw_field()
    draw_num(grid16x16_1)
    draw_footer()
    draw_selector()
    pygame.display.update()
    

