"""This python script can be used to test the correctness and finiteness of the algorithms."""
from multiprocessing import Process
from BASolver2 import bASolve, bASolverHandle
from OPBASolver import OPSolverHandle
import time

# bASolve()

class NonFiniteException(Exception):
    pass




def testcorrectness(algo):
    """"Test the algorithm specified in <algo>
    algo:
        1: BA-Algorithm
        2: OPBA-Algorithm
        3: Algorithm X
    The input will be passed to the algorithm directly
    """
    if algo == 1:
        return testBA()
    elif algo == 2:
        return testOPBA()
    elif algo == 3:
        return testAlgoX()

def locBASOLVE(grid):
    print(bASolverHandle(grid))
    # print(grid)



def testBA():
    inputs = []
    validInput = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(validInput)
    wrongdim = [[1,2,3,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]  # 4x4 instead of 9x9
    inputs.append(wrongdim)
    # 8 is two times in a collomn at start, therfore unsolvable.
    invStart = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 8, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(invStart)
    # 22 is not valid.
    invNumbers = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 22, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(invNumbers)

    emptyinp = [[0 for _ in range(9)] for _ in range(9)]
    inputs.append(emptyinp)



    for inp in inputs:
        proc = Process(target=locBASOLVE, args=[inp])
        proc.start()
        curtim = time.time()
        proc.join(timeout=11)  # This stops the test if it takes longer than 10 seconds 
        if abs(curtim-time.time()) >10:
            print("ERROR, took longer than 10 seconds. Stoped after 10 seconds")
            raise NonFiniteException("The solver took more than 10 seconds.")
        proc.terminate()
        print("NEXT")

    

def testOP():
    inputs = []
    validInput = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(validInput)
    wrongdim = [[1,2,3,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]  # 4x4 instead of 9x9
    inputs.append(wrongdim)
    # 8 is two times in a collomn at start, therfore unsolvable.
    invStart = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 8, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(invStart)
    # 22 is not valid.
    invNumbers = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 22, 0, 0, 7, 5, 0, 0, 9], [0, 0, 7, 0, 4, 0, 2, 6, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5], [0, 0, 1, 0, 5,0, 9, 3, 0], [0, 0, 0, 6, 0, 1, 0, 7, 8], [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    inputs.append(invNumbers)
    # Empty field:
    emptyinp = [[0 for _ in range(9)] for _ in range(9)]
    inputs.append(emptyinp)



    for inp in inputs:
        proc = Process(target=OPSolverHandle, args=[inp])
        proc.start()
        curtim = time.time()
        proc.join(timeout=11)  # This stops the test if it takes longer than 10 seconds 
        if abs(curtim-time.time()) >10:
            print("ERROR, took longer than 10 seconds. Stoped after 10 seconds")
            raise NonFiniteException("The solver took more than 10 seconds.")
        proc.terminate()
        print("NEXT")

    

        
            

        

        


def testOPBA():
    pass

def testAlgoX():
    pass








if __name__ == "__main__":
    # testBA()
    # testOP()
    print(bASolverHandle([[0 for _ in range(9)] for _ in range(9)]))
    