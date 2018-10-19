from functools import reduce
import operator

N = 2

matrix = [[y*x for y in range(1,N*N+1)] for x in range(1,N*N+1)]

protounique = lambda lista : len(lista)  == len(set(lista))

sliceVertical = lambda  lista, fila : list(map(lambda x : x[fila] ,lista))

def sudoku(board):
     horizontal = reduce( operator.and_, map( protounique , board))
     flippedBoard = list(map(lambda x : sliceVertical(board,x),range(N*N)))
     vertical = reduce( operator.and_, map( protounique , flippedBoard))
     return vertical and horizontal

filtro = lambda lista : list(filter(None.__ne__,lista))

print(sudoku(matrix) , sep ="\n")
