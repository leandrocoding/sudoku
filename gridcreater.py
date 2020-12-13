import solver
import exactcover
import dancesud
from makesud import make_sudoku
import pickle
import ujson

# su= next(dancesud.sudoku_solve(n=9,random=True))
# print(su)

def gen(n=1,outfile=None):

    sudlist=[]
    for i in range(n):
        sudlist.append(make_sudoku(n=9))

    # print(sudlist)
    if outfile is not None:

        with open(outfile, 'w+') as f:
        #     # pickle.dump(sudlist,pickle_file)
            ujson.dump(sudlist,f)
            # print(dum)
            # f.write(dum)
            # json_file.write()
            
    
    return sudlist


def retrive(infile):
    with open(infile, 'r') as json_file:
    #     # sudlist= pickle.load(pickle_file)
        sudlist = ujson.loads(json_file.read())
        # pickle.load()
    return sudlist


if __name__ == "__main__":
    testfile="sudoku10.json"
    gen(n=10,outfile=testfile)
    print("Recieved:")
    print(retrive(testfile))


# "sudoku.pickle"