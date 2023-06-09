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

#MUESTRA RANGO DE NUMEROS SEGUN INDICA WHILE, SINO MUESTRA EL ELSE.
#i = 1
#while i < 5:
#    print(i)
#    i += 1
#else:
#    print("else:", i)

#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
#for i in range(0, 11):
#    if i % 2 != 0:
#        print(i)

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
#x = 1
#while x < 11:
#    if x % 2 != 0:
#        print(x)
#    x+=1    

#Crea un programa con un bucle for y una sentencia break. El programa debe iterar sobre los caracteres en una dirección de 
# correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte 
# antes de @ en una línea. Usa el esqueleto de abajo:     

#for ch in "john.smith@pythoninstitute.org":
#    if ch == "@":
#        break
#    print(ch, end="")  

#Crea un programa con un bucle for y una sentenciacontinue. El programa debe iterar sobre una 
# cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena 
# modificada en la pantalla. Usa el esqueleto de abajo:

#for digit in "0165031806510":
#    if digit == "0":
#        digit="x"
#    print(digit)               #ARROJA VALOR COMO COLUMNA......


for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")         #ARROJA VALOR HORIZONTAL....
    
