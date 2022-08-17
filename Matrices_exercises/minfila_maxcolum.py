#En una matriz A(M,N) hallar los valores minimos en sus filas y los maximos en sus columna
from matrices import *
cant_filas=int(input("Ingrese la cantidad de filas: "))
cant_columnas=int(input("Ingrese la cantidad de columnas: "))
MAT=creamat(cant_filas,cant_columnas)
leemat(MAT)
imprimat(MAT)

def minimum_fila (MATRIZ):
    filas = len(MATRIZ) #se extrae el valor de la cantidad de filas
    columnas = len(MATRIZ[0]) #se extrae el valor de la cantidad de columnas
    min_fila = [0]*filas #se añade el vector que contendra a todos los valores minimos de las filas
    base = 0
    for i in range(filas):
        for j in range(columnas):
            base = MATRIZ[i][0]
            if(base < MATRIZ[i][j]):
                min_fila[i] = base
            else:
                min_fila[i] = MATRIZ[i][j]
    return min_fila
vec_min_fila = minimum_fila(MAT)
for i in range(len(vec_min_fila)):
    print("El valor minimo de la fila ",i,"es: ",vec_min_fila[i])

def maximum_col(MATRIZ):
    filas = len(MATRIZ)
    columnas = len(MATRIZ[0])
    max_colum = [0]*columnas
    base = 0
    for j in range(columnas):
        for i in range(filas):
            base = MATRIZ[0][j]
            if(base > MATRIZ[i][j]):
                max_colum[j] = base
            else:
                max_colum[j] = MATRIZ[i][j]
    return max_colum
vec_max_colum =maximum_col(MAT)
for j in range(len(vec_max_colum)):
    print("El valor maximo de la columna ",j,"es: ",vec_max_colum[j])




