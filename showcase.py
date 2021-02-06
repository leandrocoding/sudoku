import BASolver2
import makesud
import XSolver
import gridcreater
import BASolver2
import OPBASolver
import performance
# Number of Sudokus in generated Sudoku Set
n = 1

if __name__ == "__main__":
    # 1. Generate Sudoku
    tempSudoku = makesud.make_sudoku()
    print("1. Generated Sudoku:\n")
    print(XSolver.decode_sudoku_to_ascii(9,tempSudoku)) # Transform Sudoku to readable output
    generatedSudokus = gridcreater.gen(n, outfile="showcaseSudoku.json") #Generation of Sudoku Set with 1 Sudoku and saveing it to showcaseSudoku.json



    # 2. Generatiuon of Sudoku Set with n Sudokus
    print(f"\n \n2. Generated Sudoku Set with {n} Sudoku and Saved it to showcaseSudoku.json:\n")
    for i,generatedSudoku in enumerate(generatedSudokus):
        print(f"\nSudoku Nr. {i+1}")
        print(XSolver.decode_sudoku_to_ascii(9, generatedSudoku)) # Transform Sudoku to readable output




    
    # Solving with Native Backtracking
    print(f"\n \n3.1 The {n} Sudoku(s) will now be solved with the Native Backtracking Algorithm:\n")
    for i,genSud in enumerate(generatedSudokus):
    
        genSudMatrix = XSolver.exact_to_matrix(9, genSud)
        resMatrix = BASolver2.bASolverHandle(genSudMatrix)

        resexact = XSolver.matrix_to_exact(resMatrix)
   
        print(f"\nSudoku Nr. {i+1}. Solved with Native Backtracking:")
        _, resexactr = resexact
        print(XSolver.decode_sudoku_to_ascii(9, resexactr)) # Transform Sudoku to readable output





    # Solving with Advanced Backtracking
    print(f"\n \n3.2 The {n} Sudoku(s) will now be solved with the Optimized Backtracking Algorithm:\n")
    for i,genSud in enumerate(generatedSudokus):
    
        genSudMatrix = XSolver.exact_to_matrix(9, genSud)
        resMatrix = OPBASolver.advHandel(genSudMatrix)
        resexact = XSolver.matrix_to_exact(resMatrix)
   
        print(f"\nSudoku Nr. {i+1}. Solved with Optimized Backtracking:")
        _, resexactr = resexact
        print(XSolver.decode_sudoku_to_ascii(9, resexactr)) # Transform Sudoku to readable output
    
    # Solving with Algorithm X
    print(f"3.3 The {n} Sudoku(s) will now be solved with the Algorithm X:")
    for i,genSud in enumerate(generatedSudokus):
        resSud = next(XSolver.sudoku(n = 9, problem=genSud))
        print(f"\nSudoku Nr. {i+1}. Solved with Algorithm X:")
        print(XSolver.decode_sudoku_to_ascii(9, resSud)) # Transform Sudoku to readable output




    # 4. Speed Test with performance.py
    print(f"\n \n4. Executing Speedtest with the generated Sudoku Set: \n")

    normtime = performance.execute(generatedSudokus, performance.normalBacktrack)
    print(f"Native Backtracking took: {normtime:.5f} Seconds to solve {n} Sudoku(s).")
    print(f"This means the Native Backtracking Algorithm took a average of {normtime/(n+1):.5f} Seconds to solve a Sudoku.\n \n")

    advtime = performance.execute(generatedSudokus,performance.advancedBacktrack)
    print(f"Optimized Backtracking took: {advtime:.5f} Seconds to solve {n} Sudoku(s).")
    print(f"This means the Optimized Backtracking Algorithm took a average of {advtime/(n+1):.5f} Seconds to solve a Sudoku.\n \n")


    xtime = performance.execute(generatedSudokus,performance.algox)
    print(f"Algorithm X took: {xtime:.5f} Seconds to solve {n} Sudoku(s).")
    print(f"This means Algorithm X took a average of {xtime/(n+1):.5f} Seconds to solve a Sudoku.\n \n")











    
    
 





    