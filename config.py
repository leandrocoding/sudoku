
basesize = 3
resolutionField = 900
spacebelowinPX = 100
displayinHexa = False
showingSteps = True
currGrid = None
sleeptime = 0.01

solving = False


class Config:

    def __init__(self,basesize=3,resolutionField=900, spacebelowinPX=100, displayinHexa=False,sleeptime=0):
        self.basesize=basesize
        self.resolutionField=resolutionField
        self.spacebelowinPX=spacebelowinPX
        self.displayinHexa=displayinHexa
        self.sleeptime=sleeptime


class Temp:
    def __init__(self):
        self.currGrid=None


