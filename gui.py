import pygame
from config import basesize,resolutionField, spacebelowinPX, displayinHexa

pygame.init()

pygame.display.set_caption("Sudoku")
root = pygame.display.set_mode((resolutionField, resolutionField+spacebelowinPX))

# background = pygame.Surface((900,1000))
# background.fill(pygame.Color("#000000"))
root.fill((250, 250, 250))
running = True
font = pygame.font.SysFont(None, resolutionField//basesize**2)

def draw_field():
    for i in range(basesize**2+1):
        pygame.draw.line(root, (0, 0, 0), (i*resolutionField//(basesize**2), 0), (i*resolutionField//(basesize**2), resolutionField), 2)
        pygame.draw.line(root, (0, 0, 0), (0, i*resolutionField//(basesize**2)), (resolutionField, i*resolutionField//(basesize**2)), 2)

    for i in range(basesize+1):
        pygame.draw.line(root, (0, 0, 0), (0, i*resolutionField//(basesize)), (resolutionField, i*resolutionField//(basesize)), 5)
        pygame.draw.line(root, (0, 0, 0), (i*resolutionField//(basesize), 0), (i*resolutionField//(basesize), resolutionField), 5)


def draw_num(grid):
    for row in range(0,basesize**2):
        for col in range(0,basesize**2):
            num= grid[row][col]
            if num!=0:
                if displayinHexa:
                    num=hex(num).split('x')[-1]
                text = font.render(str(num), True, (0, 0, 0), (250, 250, 250))
                textRe = text.get_rect()
                textRect = textRe.move((row*resolutionField//(basesize**2)+(resolutionField//(basesize**3*1.1)), (col*resolutionField//(basesize**2)+(resolutionField//(basesize**3*2)))))
                root.blit(text,textRect)
            
        
                    
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
                   


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    root.fill((250, 250, 250))
    draw_field()
    draw_num(board)
    pygame.display.update()

