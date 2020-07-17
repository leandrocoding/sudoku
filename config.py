# Basesize:
#     Basesize defines the basesize of the sudoku Grid
#     With a Basesize of 3 the Sudoku will be 9x9 fields. This Sudoku will contain 9 squares with 9 fields

# resolutionField:
#     ResolutionField defines the hight and with, which are identical of the main sudoku Grid

# spacebelowinPX:
#     spacebelowinPX defines the amount of pixels below the main Sudoku Grid in the pygame Window.

class Config(object):
    basesize=3
    resolutionField=600
    spacebelowinPX=100
    displayinHexa=False
    sleeptime=0

class Temp(object):
    currGrid=None
