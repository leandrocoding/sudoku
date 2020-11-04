import solver
import exactcover
import dancesud
from makesud import make_sudoku
import pickle

# su= next(dancesud.sudoku_solve(n=9,random=True))
# print(su)

def gen(n=1,outfile=None):
  
    sudlist=[]
    for i in range(n):
        sudlist.append(make_sudoku(n=9))

    # print(sudlist)
    if outfile is not None:

        with open(outfile, 'wb') as pickle_file:
            pickle.dump(sudlist,pickle_file)
    
    return sudlist


def retrive(infile):
    with open(infile, 'rb') as pickle_file:
        sudlist= pickle.load(pickle_file)
        # pickle.load()
    return sudlist


if __name__ == "__main__":
    testfile="sudoku.pickle"
    gen(n=20,outfile=testfile)
    print("Recieved:")
    print(retrive(testfile))


# "sudoku.pickle"