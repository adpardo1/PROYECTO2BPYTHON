"""Primer ejercicio del proyecto Bimestral"""
"""Leer n números enteros,almacenarlos en un vector y determinar si el promedio entero de dichos números es un número primo."""
#Inicializacion y declaracion de variables
cont=0
div=0
print("Programa para determinar si el promedio de los datos ingresados en un vector es un numero primo")
print("-----------------------------------------------------------------------------------------------")
n = int(input("Ingrese el limite del vector => "))
import numpy
from random import randint
A=numpy.array([randint(1,20) for i in range(n)])
for i in range (n):
    cont=cont+A[i]
prom= (int)(cont/n)
print(A)
divi=prom
for i in range (1, divi+1):
    if prom%i==0:
        div=div + 1
if div==2:
    print("El promedio es",prom,"y ES PRIMO")
else:
    print("El promedio es",prom,"y NO ES PRIMO")


