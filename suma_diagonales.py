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
print("SUMA DE DIAGONALES DE UNA MATRIZ NxN")
CANTFILAS=int(input("Ingrese la cantidad de filas que es igual a las columnas "))
A=creamat(CANTFILAS,CANTFILAS)
print("Ingrese los valores para la matriz ")
leemat(A)
print("La matriz es: ")
imprimat(A)
SUMADP = 0 #Almacena la suma de la diagonal principal
SUMADS = 0 #Almacena la suma de la diagonal secundaria
for FILA in range(CANTFILAS):
    SUMADP = SUMADP + A[FILA][FILA]
    SUMADS = SUMADS + A[FILA][CANTFILAS-FILA-1]
print("La suma de la diagonal principal es: ",SUMADP)
print("La suma de la diagonal secundaria es: ",SUMADS)