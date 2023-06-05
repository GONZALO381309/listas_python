#variable1=input("Ingrese nombre de la planta: ")
#if variable1 == "ESPATIFILO":
#    print("Espatifilo es la mejor planta de todas!")
#elif "variable1" != "ESPATIFILO":
#    print("No, ¡quiero una gran ESPATIFILO!")
#else: print("¡ESPATIFILO!, No", [variable1])

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

#odd_numbers = 0
#even_numbers = 0

# Lee el primer número.
#number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
#while number != 0:
    # Verificar si el número es impar.
 #   if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
  #      odd_numbers += 1
   # else:
        # Incrementar el contador de números pares even_numbers.
    #    even_numbers += 1
    # Leer el siguiente número.
#    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
#print("Cuenta de números impares:", odd_numbers)
#print("Cuenta de números pares:", even_numbers)

#JUEGO 

#secret_number = 777

#print(
#"""
#+==================================+
#| ¡Bienvenido a mi juego, muggle!  |
#| Introduce un número entero       |
#| y adivina qué número he          |
#| elegido para ti.                 |
#| Entonces,                        |
#| ¿Cuál es el número secreto?      |
#+==================================+
#""")
#secret_number=int(input("Ingresa minumero secreto ahora: "))
#while secret_number != 777:
 #   print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
   # secret_number=int(input("Ingresa minumero secreto ahora: "))
  #  if secret_number == 777:
  #      print("¡Bien Hecho, Muggle! Eres Libre ahora")

#CONTEO DE SEGUNDO DE MANERA INTERNA
#import time

#for i in range(1,6): # Escribe un bucle for que cuente hasta cinco.
#    print(i,"Mississippi")# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
#    usar: time.sleep (1) # Cuerpo del bucle - usar: time.sleep (1)

#print("¡Listos o no, ahí voy!") # Escribe una función de impresión con el mensaje final.

#IDENTIFICACIÓN DE NUMEROS MAS GRANDES CON CICLO WHILE
#largest_number = -99999999
#counter = 0

#while True:
#    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#    if number == -1:
#        break
#    counter += 1
#    if number > largest_number:
#        largest_number = number#

#if counter != 0:
#    print("El número más grande es", largest_number)
#else:
#    print("No has ingresado ningún número.")


i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

