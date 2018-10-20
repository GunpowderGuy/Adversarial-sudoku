from functools import reduce
import operator

N = 2

matrix = [[y*x for y in range(1,N*N+1)] for x in range(1,N*N+1)]

x = list(map(lambda x:x[:2], matrix))

protounique = lambda lista : len(lista)  == len(set(lista))

sliceVertical = lambda lista, columna: list(map(lambda x : x[fila] ,lista))

def mul(x,y):
    if x == 0 and y != 0 :
        x = 1
    if y == 0 and x != 0 :
        y = 1
    return x*y

def cuandrantes(lista):
    result = list(map(lambda x : [] , range(N*N)))
    for cuadrante in range(N*N):
        for y in range(N*N):
            for x in range(N):
                if x < mul(N,cuadrante) and y < mul(N,cuadrante):
                #result[y].insert([y][x],lista)
                    result[cuadrante].append(lista[y][x])
    return result


def sudoku(board):
     horizontal = reduce( operator.and_, map( protounique , board))
     flippedBoard = list(map(lambda x : sliceVertical(board,x),range(N*N)))
     vertical = reduce( operator.and_, map( protounique , flippedBoard))
     return vertical and horizontal

filtro = lambda lista : list(filter(None.__ne__,lista))

matriz = [
[1,0,0,2],
[0,0,0,0],
[0,0,0,0],
[3,0,0,4],
]

print(cuandrantes(matriz), sep ="\n")
