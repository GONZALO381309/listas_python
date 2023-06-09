import numpy as np
#MUESTRA 100 NUMEROS ENTRE 0 Y 500
#arreglo_A=range(0,100)
#arreglo=np.array(arreglo_A)
#for n in arreglo_A:
#  arreglo[n]=np.random.randint(0,500)
#print(arreglo)

#print("La posición del elemento mayor es: ")
#print("El numero máximo: ",arreglo.max())
#print("El numero minimo: ",arreglo.min())
#print("El numero sumatoria: ",arreglo.sum())
#print("El numero promedio: ",arreglo.mean())

#PARA SACAR NUMEROS PARES DE UNA LISTA entre 0 y 500

#lista=[i for i in range(0,500) if i % 2 == 0]
#print(lista)

#PRUEBA DE VALIDACION NUMEROS PARES SEGUN LISTA DEFINIDA EN PRIMER PUNTO
#list=[arreglo_A for arreglo_A in range(0,500) if arreglo_A % 2 == 0]
#print(list)


#EJERCICIO 2

import random 
#x=range (0,10)
#numero_aleatorio=np.random.randint(0,10)
#for i in x:
#    print(i)
#c=np.array([np.random.randint(0,1000) for i in x])
#print(c)


#EJERCICIO 1

Lista=[]
for _ in range(10):
    numero_aleatorio=random.randint(0,500)
    Lista.append(numero_aleatorio)
    if numero_aleatorio % 2 == 0:
        print("Los numeros pares son: ",numero_aleatorio)
Lista.append(501)
Lista.insert(0,501)
arreglo=np.array(Lista)
print("Este es el numero maximo: ", arreglo.max())
print("Esta en la posición: ",Lista.index(arreglo.max()))
print(arreglo)
valor_maximo=arreglo.max()
for i in range(len(arreglo)):
    if arreglo[i] == valor_maximo:
        print("La posicion del valor maximo es: ", i)

