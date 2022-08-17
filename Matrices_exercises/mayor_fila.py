from matrices import *
print("PROGRAMA QUE SACA EL MAYOR NUMERO DE CADA FILA")
cant_filas=int(input("Ingrese la cantidad de filas de la matriz: "))
cant_columnas=int(input("Ingrese la cantidad de columnas de la matriz: "))
A = creamat(cant_filas,cant_columnas) #Se crea la matriz A con M filas y N columnas
leemat(A) #Se asigna valores por teclado a la matriz A
imprimat(A) #Se muestra el contenido de la matriz A
max_fila = [0]*cant_filas
for i in range(cant_filas):
    for j in range(cant_columnas):
        base = A[i][0]
        if base < A [i][j]:
            max_fila[i] = A[i][j]
        else:
            max_fila[i] = base
for i in range(cant_filas):
    print("El mayor valor de la fila ",i,"es: ",max_fila[i])


