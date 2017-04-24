from Matrix import Matrix
from random import randint

def fill_sudoku(m):
    rowNum = len(m)
    for row in range(rowNum):
        colNum = len(m[row])
        for col in range(colNum):
            m.set_at(row, col, randint(1, 9))

m = Matrix(9, 9)
fill_sudoku(m)
print(m)

