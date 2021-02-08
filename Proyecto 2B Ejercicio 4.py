"""Ejercicio 4 del proyecto"""
#Inicializacion y declaracion de variables
band=False
nn=0
print("Programa para buscar un numero dentro de un arreglo")
print("---------------------------------------------------")
print(" ")
n=int(input("Ingrese el limite de numeros = "))
print(" ")
import numpy
import random 
A=[0]*n
#Se generan los valores aleatorios para el vector
for i in range(n):
    A[i]=random.randint(1,9)
#Se imprime el vector 
print(A)
print(" ")
print("---------------------------------------------------")
print(" ")
x=int(input("Ingrese el elemento a buscar = "))
while ((band==False)and(nn<n)):
    if (A[nn]==x):
        band=True
        print("El numero ",x," si se encuentra en la lista")
    nn=nn+1
if band==False:
    print("El numero ",x," no se encuentra en la lista")
