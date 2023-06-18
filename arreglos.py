import numpy as np
#forma 1 desde lista
#lista=[1,2,3,4]
#listb=[5,6,7,8]
#arr= np.array(lista)
#arr= np.array(listb)
#print(arr)

#forma 2 directa
#arr2=np.array([5,6,7,8])
#print(arr2)


#funciones con arreglo
arreglo=np.array([5,6,7,8,9,10,11,12])
print(arreglo.ndim)
print("El largo del arreglo es: ",len(arreglo))
print("Mostrar desde 4 psicion a la sexta posicion", arreglo[4:6])
print(arreglo[0:7:2])
print(arreglo[::2])
c=[i for i in range (0,101)]
print(c[1:100:2]) #impares
print(c[0:100:2])


#arreglo=np.array ([4,8,15,16,23,42])
#contar_hasta=len(arreglo)
#for i in range (contar_hasta):
    #imprime el contenido individual
#    print(arreglo[i])

#imprimiendo el arreglo
#print(arreglo)

#crear un acceso directo a un arreglo
#arreglo_copia=arreglo[:]

#copia real
#arreglo_copia=arreglo[:].copy()
#arreglo[0]=1000

#print("Original", arreglo)
#print("Copia", arreglo_copia)