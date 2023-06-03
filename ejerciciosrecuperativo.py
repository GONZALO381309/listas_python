import numpy as np

arreglo_A=range(0,100)
arreglo=np.array(arreglo_A)
for n in arreglo_A:
   arreglo[n]=np.random.randint(0,500)
print(arreglo)

for j in arreglo:
   if arreglo % 2 == 0:
      print(arreglo)

 


print("La posición del elemento mayor es: ")
print("El numero máximo: ",arreglo.max())
print("El numero minimo: ",arreglo.min())
print("El numero sumatoria: ",arreglo.sum())
print("El numero promedio: ",arreglo.mean())
