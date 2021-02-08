"""Segundo ejercicio del proyecto Bimestral"""
"""Leer una matriz 4x6 entera y determinar en qué posiciones están los menores pares por fila."""
#Inicializacion de variables
aux=100
print("Programa que determine en que posiciones estan los numeros menores por filas en una matriz de 4x6")
print("-------------------------------------------------------------------------------------------------")
print("Se generan valores aleatorios en la matriz A")
import numpy
from random import randint
A=[]
for i in range(4):
    A.append([])
    for j in range(6):
        A[i].append(randint(1,9))
#Se presenta la matriz
for i in range (4):
    for j in range (6):
        print(A[i][j], end=' ')
    print(' ')
#Se realizan el proceso para encontrar los menores pares
for i in range(4):
    for j in range(6):
        if ((A[i][j]%2==0)and(A[i][j]<aux)):
            aux=A[i][j]
    #presentamnos los menores por fila
    print("Fila: ",i)
    for j in range(6):
        if A[i][j] == aux:
            print("Se ha encontrado el menor par en A[",i,"][",j,"] = ",aux)
    aux=100



