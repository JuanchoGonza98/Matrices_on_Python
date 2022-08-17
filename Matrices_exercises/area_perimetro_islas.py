# Hallar el perímetro y la superficie de una isla en matriz A MxN
from matrices import *

print("HALLAR EL PERIMETRO Y AREA DE UNA ISLA EN UNA MATRIZ\n")
ESCALA = int(input("Ingrese la longitud del lado de cada celda = "))
A =  [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0]]
FIL = 4
COL = 5
imprimat(A)
PERIMETRO = 0
AREA = 0
cant_unos = 0
# Barrido horizontal de la matriz
for FILA in range(FIL - 1):
    for COLUM in range(COL - 1):
        if A[FILA][COLUM] == 1:
            cant_unos = cant_unos + 1
        if A[FILA][COLUM] != A[FILA][COLUM + 1]:
            PERIMETRO = PERIMETRO + 1
# Barrido vertical de la matriz
for COLUM in range(COL - 1):
    for FILA in range(FIL - 1):
        if A[FILA][COLUM] != A[FILA + 1][COLUM]:
            PERIMETRO = PERIMETRO + 1

PERIMETRO = PERIMETRO * ESCALA
AREA = cant_unos * ESCALA ** 2
print("El perímetro de la isla es de ", PERIMETRO, "metros")
print("El área de la isla es de ", AREA, "metros cuadrados")
