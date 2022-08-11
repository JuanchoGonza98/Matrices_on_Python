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
print("Suma de Columnas de la matriz A")
CANTFILAS=int(input(print("Ingrese la cantidad de filas: ")))
CANTCOLUM=int(input(print("Ingrese la cantidad de columnas: ")))
A=creamat(CANTFILAS,CANTCOLUM)
SUMACOL=[0]*CANTCOLUM
print("Ingrese los valores para la matriz A:")
leemat(A)
print("La matriz es: ")
imprimat(A)
for J in range(CANTCOLUM):
    for I in range(CANTFILAS):
        SUMACOL[J]= SUMACOL[J] + A[I][J]
for I in range(CANTCOLUM):
    print("La suma de la columna",I,"es: ",SUMACOL[I])
