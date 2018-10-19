N = 2

nomatrix = [[0 for y in range(N*N)] for x in range(N*N)]

protounique = lambda lista : len(lista)  == len(set(lista))

filtro = lambda lista : list(filter(None.__ne__,lista))

print(filtro([None,1]) , sep ="\n")
