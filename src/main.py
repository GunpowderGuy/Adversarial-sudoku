from functools import reduce
import operator

N = 2

matrix = [[0 for y in range(N*N)] for x in range(N*N)]

protounique = lambda lista : len(lista)  == len(set(lista))

# sliceVertical = lambda  lisa, fila : list(map(lambda x : x[fila] ,lista))

def sudoku(board):
     horizontal = reduce( operator.and_, map( protounique , board))
     return horizontal


filtro = lambda lista : list(filter(None.__ne__,lista))

print(sudoku(matrix) , sep ="\n")
