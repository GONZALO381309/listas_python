import numpy as np
import random
#VARIABLES DE INFORMACION DE INFORMACION VEHICULO
marca=(2,15)
#----------------------------------------------------
opcion=0
opcion_info_vehi=0
lista=[]
multas=0
menu_act=True
er=True
#ALMACENAMIENTO DE INFORMACION VEHICULAR
tipo_almacenado=0
patente_almacenado=0        
marca_almacenado=0
precio_almacenado=0
multas_almacenado=0
multas_almacenado1=0
fecha_registro_almacenado=0
nombre_dueno_almacenado=0
#VARIABLES DE OPCION 3
valor_certificado=(1500,3500)
print("Bienvenido a la Automotora AUTO SEGURO")
while menu_act:
    print("Selecciones una de las siguientes opciones para acceder:")
    print()
    print("1. GRABAR")
    print("2. BUSCAR")
    print("3. IMPRIMIR CERTIFICADOS")
    print("4. SALIR")

    opcion=int(input("Ingrese una de las siguientes opciones: "))

    if opcion == 4:
        print("Usted ha seleccionado la opcion 4.- SALIR")
        print("Gonzalo Cortez")
        print("Versión del Programa: 1.0")
        break