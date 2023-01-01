"""
author: Andrew S Erwin
link: https://github.com/erwininteractive

Backtracking algorithm to solve sudoku puzzles
"""
import numpy as np

puzzle =  [[0,0,9,0,3,0,1,0,0],
           [4,0,0,1,0,0,0,9,0],
           [0,5,0,0,0,4,6,0,0],
           [0,0,0,7,0,3,5,0,0],
           [0,8,0,0,0,0,0,2,0],
           [0,0,1,4,0,5,0,0,0],
           [0,0,7,2,0,0,0,5,0],
           [0,2,0,0,0,8,0,0,7],
           [0,0,5,0,1,0,2,0,0]]

def isPossible(x,y,n) :
    global puzzle

    for i in range(9) :
        if puzzle[y][i] == n :
            return False
    
    for i in range(9) :
        if puzzle[i][x] == n :
            return False
    
    x0 = (x//3)*3
    y0 = (y//3)*3
    
    for i in range(3) :
        for j in range(3) :
            if puzzle[y0+i][x0+j] == n :
                return False
    
    return True

def solve() :
    global puzzle
    
    for y in range(9) :
        for x in range(9) :
            if puzzle[y][x] == 0 :
                for n in range(1,10) :
                    if isPossible(x,y,n) :
                        # Try n
                        puzzle[y][x] = n

                        # solve to test n
                        solve()

                        # It didn't work! Putting it back to 0
                        puzzle[y][x] = 0
                return
    
    print(np.matrix(puzzle))

solve()
