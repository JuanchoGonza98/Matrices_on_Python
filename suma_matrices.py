#Crear una matriz conociendo la cantidad de filas  Columnas
def creamat (M,N): #se crea la funcion creamat que recibe dos numeros M para fila y N para columnas
    MATRIZ = []  #Se indica el nombre para la matriz
    for I in range(M):
        MATRIZ.append([0] * N)
    return (MATRIZ)

def leemat (MATRIZ): #funcion que sirve para introducir datos a la matriz
    M = len(MATRIZ)
    N = len(MATRIZ[0])
    for I in range(M):
        for J in range(N):
            MATRIZ[I][J]= float(input("Ingrese el elemento: (%d,%d):" % (I,J)))

def imprimat (MATRIZ):
    FILAS = len(MATRIZ)
    for I in range(FILAS):
        print (MATRIZ[I])

print("SUMA DE MATRICES\n")
CANFIL= int(input("Ingrese la cantidad de filas: "))
CANCOL = int(input("Ingrese la cantidad de columnas: "))
A=creamat(CANFIL,CANCOL)
B=creamat(CANFIL,CANCOL)
C=creamat(CANFIL,CANCOL)
print("Ingrese los valores para la matriz A")
leemat(A)
print("Ingrese los valores para la matriz B ")
leemat(B)
for FILA in range(CANFIL):
    for COL in range(CANCOL):
        C[FILA][COL] = A[FILA][COL] + B[FILA][COL]
print("La matriz suma es: ")
imprimat(C)

