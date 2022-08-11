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
#Primero se deben tener la cantidad de filas y columnas para crear la matriz
CANTFILAS = int(input("Ingrese la cantidad de filas de la matriz A: "))
CANTCOLUMNAS = int(input("Ingrese la cantidad de columnas de la matriz A: "))
A=creamat(CANTFILAS,CANTCOLUMNAS) #Se procede a crear la matriz A con valor 0 cada posicion
#Se debe introducir los valores a la matriz
leemat(A)
#Una vez se tengan los datos de la matriz se debe ingresar el numero k por el que se va a multiplicar
k=float(input("Ingrese el numero que multiplicara a la matriz A: "))
#El producto de la matriz A creara otra matriz C entonces hay que crear esa matriz
C=creamat(CANTFILAS,CANTCOLUMNAS)
for I in range(CANTFILAS):
    for J in range(CANTCOLUMNAS):
        C[I][J] = A[I][J] * k
print("La matriz producto entre A * k es ")
imprimat(C)



