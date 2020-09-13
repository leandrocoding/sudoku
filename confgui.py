import dearpygui.dearpygui as dpg
from config import Config as c,Temp as t
from gui import run
from multiprocessing import Process
from testGrids import Grids
import copy
from threading import Thread
from advsolve import findPossi



# Callbacks

def butcallback(sender, data):
    basesize=dpg.get_value(name="Basesize")
    sleeptime=dpg.get_value(name="Delay in ms")/1000
    print(f"Basesize: {basesize}")
    print(sleeptime)

def updateconfig(sender,data):
    c.basesize=dpg.get_value("Basesize")
    c.sleeptime=dpg.get_value("Delay in ms")/1000

def startPygame(sender,data):
    
    if not t.pygameActive:
        
        
        t.pygameActive=True
        
        dpg.run_async_function("asyncrun",())
    else:
        print("Pygame is already running")


def asyncrun(s,d):
    run()

def resetGrid(s=None,d=None):
    t.currGrid = copy.deepcopy(Grids.gridBases[c.basesize]["Easy1"])
    print(findPossi(t.currGrid))


def stopSudoku(s,d):
    t.pygameActive=False
    print("Pygame Stoping")

def clearGrid(s,d):
    t.currGrid=grid = [[0 for i in range(c.basesize**2)]for j in range(c.basesize**2)]

def setGridone(s,d):
    t.currGrid = copy.deepcopy(Grids.gridBases[c.basesize]["Easy1"])
def setupconfig():
    dpg.set_main_window_size(600,300)
    dpg.set_main_window_title("Sudoku Config")


    dpg.add_text(name="Sudoku Config")
    dpg.add_slider_int(name="Basesize",default_value=c.basesize,min_value=2,max_value=5,callback="updateconfig")
    dpg.add_slider_float(name="Delay in ms",default_value=c.sleeptime*1000,min_value=0,max_value=400,callback="updateconfig")



    # dpg.add_button(name="Print Values",callback="butcallback")

    dpg.add_button(name="Start Solver",callback="startPygame")
    dpg.add_same_line()
    dpg.add_button(name="Stop Pygame",callback="stopSudoku")

    dpg.add_button(name="Reset Grid",callback="resetGrid")
    
    
    dpg.add_same_line()
    dpg.add_button(name="Set a Grid",callback="setGridone")

    # dpg.add_listbox(name="Grid Selection",items=Grids.gridBases[3])


def confguirun():
    dpg.start_dearpygui()



if __name__ == "__main__":
    setupconfig()
    confguirun()
