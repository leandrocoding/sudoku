#!/usr/bin/env python

"""This module is the file handler.
You can generate a json file with Sudokus with gen(n = <Number of Sudokus to be generated>, outfile = <path of outputfile>).
To retrieve Sudokus from a json file use retrive_json(<File name>)

"""

import BASolver as solver
import exactcover
import XSolver as dancesud
from makesud import make_sudoku
import pickle  # Legacy
import ujson



def gen(n=1,outfile=None):
    """Generate <n> Sudokus and store them in the json file at <outfile>"""

    sudlist=[]
    print(f"Generating {n} Sudokus.")
    for i in range(n):
        print(f"{i}/{n} --> {i/n*100:.1f}%",end="\r")

        sudlist.append(make_sudoku(n=9))
    print(f"{n} Sudokus generated and saved in {outfile}")
    if outfile is not None:

        with open(outfile, 'w+') as f:
            ujson.dump(sudlist,f)
    return sudlist


def retrive_pickle(infile):
    """Retrieve Sudokus form pickle file. (LEGACY, use retrive_json when possible)"""
    with open(infile, 'rb') as pickle_file:
        sudlist= pickle.load(pickle_file)

    return sudlist

def retrive_json(infile):
    """Retrieve Sudokus form json file."""
    with open(infile, 'r') as json_file:

        outtt = json_file.read()

        sudlisttemp = ujson.loads(outtt)
        # This converts the lists inside into touples this is necessary because to search a dict you need a touple.
        sudlist= list(map(lambda inpp: list(map(tuple, inpp)), sudlisttemp))
    return sudlist
if __name__ == "__main__":
    testfile="finallSudoku1000.json"
    gen(n=1000,outfile=testfile)
    print("Recieved:")
    print(retrive_json(testfile))
