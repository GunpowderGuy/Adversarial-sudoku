from functools import reduce
import operator

N = 2

matrix = [[y*x for y in range(N*N)] for x in range(N*N)]

protounique = lambda lista : len(lista)  == len(set(lista))

sliceVertical = lambda  lista, fila : list(map(lambda x : x[fila] ,lista))

def sudoku(board):
     # horizontal = reduce( operator.and_, map( protounique , board))
     flippedBoard = list(map(lambda x : sliceVertical(board,x),range(N*N)))
     return flippedBoard

filtro = lambda lista : list(filter(None.__ne__,lista))

print(matrix , sep ="\n")
