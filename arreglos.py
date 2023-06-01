import numpy as np
#forma 1 desde lista
lista=[1,2,3,4]
arr= np.array(lista)
#print(arr)

#forma 2 directa
arr2=np.array([5,6,7,8])
#print(arr2)


#funciones con arreglo
arreglo=np.array([5,6,7,8,9,10,11,12])
#print(arreglo.ndim)
#print(len(arreglo))
#print(arreglo[4:7])
#print(arreglo[0:7:2])
#print(arreglo[::2])
c=[i for i in range (0,101)]
print(c[1:100:2]) #impares
print(c[0:100:2])