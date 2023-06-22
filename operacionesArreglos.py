import numpy as np
#numeros_aleatorios=np.random.randint(0,100)
#print(numeros_aleatorios)

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto del 0 | 
| al 20?                           |
+==================================+
""")
ingre_numero=0

x=range(1)
arreglo=np.array(x)

#for n in x:
ingre_numero=int(input("Ingrese numero para salir del bucle: "))
arreglo=np.random.randint(1,20)
while ingre_numero != arreglo:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    ingre_numero=int(input("Ingrese numero para salir del bucle: "))
    if ingre_numero == arreglo:
        print("¡Bien Hecho, Muggle! Eres Libre ahora")
print("El numero secreto fue: ", arreglo)


#print("El numero máximo: ",arreglo.max())
#print("El numero minimo: ",arreglo.min())
#print("El numero sumatoria: ",arreglo.sum())
#print("El numero promedio: ",arreglo.mean())