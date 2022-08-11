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
print("MULTIPLICACION DE MATRICES A * B\n")
CANFILA = int(input("Ingrese la cantidad de filas de A = "))
CANCOLA = int(input("Ingrese la cantidad de columnas de A = "))
CANCOLB = int(input("Ingrese la cantidad de columnas de B"))
A=creamat(CANFILA,CANCOLA)
B=creamat(CANCOLA,CANCOLB)
PRODUCTO=creamat(CANFILA,CANCOLB)
print("Ingrese los valores para la matriz A")
leemat(A)
print("Ingrese los valores para la matriz B")
leemat(B)
for FILA in range (CANFILA):
    for COL in range (CANCOLB):
        SUMA = 0
        for K in range (CANCOLA):
            SUMA = SUMA + A[FILA][K] * B[K][COL]
            PRODUCTO[FILA][COL] = SUMA
print("La matriz producto es")
imprimat(PRODUCTO)
