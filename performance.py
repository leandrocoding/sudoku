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
    
    time = execute(sudoku_set,normalBacktrack,n)
    timeoutput(outfile, time,"Normal Backtracking",n)
    print(f"Normal Backtracking done in {time} seconds")
    sleep(1)
    time2 = execute(sudoku_set,advancedBacktrack,n)
    timeoutput(outfile, time2,"Advanced Backtracking",n)
    print(f"Advanced Backtracking done in {time2} seconds")
    sleep(1)
    time3 = execute(sudoku_set,dancingLink,n)
    timeoutput(outfile, time3,"Dancing Links",n)
    print(f"Dancing Links done in {time3} seconds")
    sleep(1)
    print(f"Finished in {time+time2+time3} seconds")
    # sleep(10)  # will be buch higher in production, to idle between algos



def timeoutput(outfile, time, method, n):
    with open(outfile,"a+") as f:
        f.write(f"Solved a set of sudokus {n} {'time' if n==1 else 'times'} in {time} Seconds using the {method} algorithm.\n\r")






def execute(sud_set,method, n):
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
    main(infile="sudoku700.pickle",outfile="sudokutime700.txt",n=1)
