"""Tercer ejercicio del proyecto bimestral"""
"""Construir una función que reciba como parámetro una matriz 4x4 entera y retorne el número de la columna en donde se encuentre por primera vez el número mayor de la matriz"""
#Inicializacion de variables
def MAYOR():    
    import numpy
    from random import randint
    A=[]
    for i in range(4):
        A.append([])
        for j in range(4):
            A[i].append(randint(1,9))
    #Se presenta la matriz
    for i in range (4):
        for j in range (4):
            print(A[i][j], end=' ')
        print(' ')
        
    mayor=0
    bandera = False
    for i in range (4):
        for j in range (4):
            if A[i][j] > mayor:
                mayor=A[i][j]
        for j in range (4):
            if ((A[i][j]==mayor)and(bandera==False)):
                print("El numero mayor es el ",mayor," y se encuentra por primera vez en la columna ",j," fila ",i)
                bandera = True

                
print("Programa que determine el número de la columna en donde se encuentre por primera vez el número mayor de la matriz de 4x4")
print("------------------------------------------------------------------------------------------------------------------------")
print("Se generan valores aleatorios para la matriz A")

MAYOR()

                
    
