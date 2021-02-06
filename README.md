# Implementations of three Sudoku Solving algorithms
**This is part of the Matura Project of Leandro Zazzi.**  
This is the Source Code of the implementations of the analyzed algorithms. 
The three algorithms that were analyzed are:
1. Native Backtracking Algorithm
1. Optimized Backtracking Algorithm
1. Algorithm X 


## Setup
1. Download a copy of the newest version of this Repository. This can either be done by clicking Download ZIP in the upper right corner or by running the following command:
> git clone https://github.com/leandrocoding/sudoku.git
2. Make sure Python 3.9 is installed on your system.
1. Install the packages ujson and pygame.
This can be done by typing the following in to the commandline. (In some cases you have to replace python with python3 or py or py3)
> python -m pip install ujson pygame   

## All in one showcase
The file showcase.py can be executed and shows the most important things of this Project.  
It should also be possible to undestand how the different Algorithms get execuzted looking at this file.
In this showcase all the algorithms will be executed and all the tests. As a input it uses one Sudoku. This Sudoku can be found in the file.
At the top of the file there is a variable n which can be modified. n is the number of Sudokus in the generated Sudoku Set which will also be used to test the Sudokusolvers. 
This file will do the following when executed:
1. A Sudoku gets generated and printed to the console.
1. Generate a Sudoku set with 1 Sudoku as showcaseSudoku.json
1. This Sudoku will be solved by the three algorithms. It will always print the result to the console. 
1. The time will be measured for the three Algorithms using performance.py

To run the Tests for Correctness and finiteness run evaluations.py





## Extra

You can run the Graphical Sover by executing gui.py.
The Controls are the following:
S: Solve Sudoku
R: Reset Grid (Generates a new Sudoku)
Arrowkeys: Move the Selector
Mouse leftclick: Move Selector to mouse.
Numbers 1-9: Set the corresponding Number in the field.
Del: Clear the field.
Ctrl / Shift: Change Solver (Only Native Backtracking Supported atm.)

This Solver only supports the Native Backtracking algorithm at the moment.


