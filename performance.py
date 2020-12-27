#!/usr/bin/env python3

import cProfile
from gridcreater import retrive_json
from time import sleep, perf_counter
import XSolver as ds
import BASolver as basicsolver
import BASolver2 as bs2
import OPBASolver as advsolve



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



    sudoku_set = retrive_json(infile)
    with open(outfile,"a+") as f:
        f.write("\n\r\n\r==============================================")
        f.write("==============================================\n\r")
        f.write(f"Start of Benchmark with {n} executions of the set with {len(sudoku_set)} sudokus.\n\r")
        f.write("==============================================\n\r")
    for m in range(n):
        time = execute(sudoku_set,normalBacktrack)
        timeoutput(outfile, time,"Normal Backtracking",m)
        print(f"Normal Backtracking done in {time} seconds")
        sleep(60*5)  # Waiting 5 minutes between executing the algorithms.
        time2 = execute(sudoku_set,advancedBacktrack)
        timeoutput(outfile, time2,"Advanced Backtracking",m)
        print(f"Advanced Backtracking done in {time2} seconds")
        sleep(60*5)  # Waiting 5 minutes between executing the algorithms.
        time3 = execute(sudoku_set,algox)
        timeoutput(outfile, time3,"Dancing Links",m)
        print(f"Dancing Links done in {time3} seconds")
        print(f"Finished in {time+time2+time3} seconds")
        sleep(60*5)  # Waiting 5 minutes between executing the algorithms.





def timeoutput(outfile, time, method, n):
    """Writes Measurements to <outfile>"""
    with open(outfile,"a+") as f:
        f.write(f"Solved a set of sudokus in {time:.3f} Seconds using the {method} algorithm.\n\r")



def executeMe1():
    """This gets executed with the profiler."""
    infile = "sudoku1.json"
    sudoku_set = retrive_json(infile)
    for sud in sudoku_set:
        normalBacktrack(sud)
        # advancedBacktrack(sud)
        # algox(sud)





def profiling():
    """Profiling to analyze the algorithms in detail."""
    cProfile.run("executeMe1()",)





def execute(sud_set,algorithm):
    """Measures the time of execution time for a algorithm for a set of Sudoukus with """
    tic= perf_counter()
    # Do stuff
    for sud in sud_set:
        algorithm(sud)
    toc=perf_counter()
    return toc-tic


def normalBacktrack(sud):
    """ Interface for Native Backtracking """
    
    bo=ds.exact_to_matrix(9, sud)
    
    bs2.bASolve(bo)
    


def advancedBacktrack(sud):
    """ Interface for Native Backtracking """

    abc=[]
    bo= ds.exact_to_matrix(9, sud)
    advsolve.solveadv(bo,sols=abc)

def algox(sud):
    """ Interface for Algorithm X """

    ds.sudoku_solve(problem=sud)

if __name__ == "__main__":
    main(infile="finallSudoku1000.json",outfile="outsud/finalout.txt",n=1)
    # main(infile="sudoku1.json",outfile="outsud/sut22.txt",n=1)
    # profiling()
    # executeMe1()
