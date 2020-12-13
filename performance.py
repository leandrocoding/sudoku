#!/usr/bin/env python3

import cProfile
from gridcreater import retrive
from time import sleep, perf_counter
import dancesud as ds
import solver as basicsolver
import advsolve



def main(infile=None,outfile=None,n=None):
    """
    Function to test algorithms

    :param infile: Path of Pickle file with sudokus
    :param outfile: Name of text file with stats about solver
    """
    print("This programm compares the three algorithms to solve Sudokus")
    if infile is None:
        infile = input("Path to input file: ")
    if outfile is None:
        outfile = input("Path to output file: ")
    if n is None:
        try:
            n = int(input("Number of times executed: "))
        except ValueError:
            print("Invalid input, using 1.")
            n=1
    


    sudoku_set = retrive(infile)
    with open(outfile,"a+") as f:
        f.write("\n\r\n\r==============================================")
        f.write("==============================================\n\r")
        f.write(f"Start of Benchmark with {n} executions of the set with {len(sudoku_set)} sudokus.\n\r")
        f.write("==============================================\n\r")
    for m in range(n):
        time = execute(sudoku_set,normalBacktrack)
        timeoutput(outfile, time,"Normal Backtracking",m)
        print(f"Normal Backtracking done in {time} seconds")
        sleep(60*5)
        time2 = execute(sudoku_set,advancedBacktrack)
        timeoutput(outfile, time2,"Advanced Backtracking",m)
        print(f"Advanced Backtracking done in {time2} seconds")
        sleep(60*5)
        time3 = execute(sudoku_set,dancingLink)
        timeoutput(outfile, time3,"Dancing Links",m)
        print(f"Dancing Links done in {time3} seconds")
        print(f"Finished in {time+time2+time3} seconds")
        sleep(60*5)
    
    # sleep(10)  # will be buch higher in production, to idle between algos



def timeoutput(outfile, time, method, n):
    with open(outfile,"a+") as f:
        f.write(f"Solved a set of sudokus {n} {'time' if n==1 else 'times'} in {time:.3f} Seconds using the {method} algorithm.\n\r")

def executeMe1():
    # infile = "sudoku700.pickle"
    infile = "sudoku.pickle"
    sudoku_set = retrive(infile)
    for sud in sudoku_set:
        # normalBacktrack(sud)
        # advancedBacktrack(sud)
        dancingLink(sud)





def profiling():
    cProfile.run("executeMe1()",)
    




def execute(sud_set,method):
    tic= perf_counter()
    # Do stuff
    for sud in sud_set:
        method(sud)
    toc=perf_counter()
    return toc-tic
    

def normalBacktrack(sud):
    abc=[]
    bo=ds.exact_to_matrix(9, sud)
    basicsolver.solve(bo,sols=abc)


def advancedBacktrack(sud):
    abc=[]
    bo= ds.exact_to_matrix(9, sud)
    advsolve.solveadv(bo,sols=abc)
    
def dancingLink(sud):
    ds.sudoku_solve(problem=sud)

if __name__ == "__main__":
    main(infile="sudoku700.pickle",outfile="sut2.txt",n=1)
    # profiling()
