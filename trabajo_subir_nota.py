import numpy as np
import random
#VARIABLES DE INFORMACION DE INFORMACION VEHICULO
opcion=0
opcion_info_vehi=0
lista=()
multas=0
menu_act=True
marca_activa=True
opcion_certificado=0
#ALMACENAMIENTO DE INFORMACION VEHICULAR
tipo_almacenado=0
patente_almacenado=0      
marca_almacenado=0
precio_almacenado=0
multas_almacenado=0
multas_almacenado1=0
fecha_registro_almacenado=0
nombre_dueno_almacenado=0
alma_fecha_multas=0
certificado_act=True
solicitar_certificado_adicional=0
#VARIABLES DE OPCION 3
valor_certificado=(1500,3500)
print("--------------------------------------")
print("Bienvenido a la Automotora AUTO SEGURO")
print("--------------------------------------")
while menu_act:
    print("Selecciones una de las siguientes opciones para acceder:")
    print()
    print("1. GRABAR")
    print("2. BUSCAR")
    print("3. IMPRIMIR CERTIFICADOS")
    print("4. SALIR")

    opcion=int(input("Ingrese una de las siguientes opciones: "))
    if opcion == 1:
        print("Usted seleccionado opcion 1.- GRABAR")
        print("1. Ingreso información de vehículos:\nTipo \nPatente \nMarca \nPrecio \nmultas \nFecha Registro Vehículo \nNombre Dueño")
        opcion_info_vehi=int(input("Presione 1 para ingreso de datos: "))
             
        if opcion_info_vehi == 1:
            tipo=input("Ingrese tipo de vehículo: ")
            tipo_almacenado=tipo
            patente=input("Ingrese patente vehicular: ")
            print("Ha ingresado la patente correcta?\n1.SI,\n2.NO")
            validacion_patente=int(input())
            if validacion_patente == 1:
                patente_almacenado=patente
            if validacion_patente == 2:
                patente=input("Ingrese patente vehicular: ")
                patente_almacenado=patente
            marca=input("Ingrese marca del vehiculo: ")
            caracteres=len(marca)
            for i in marca:
                if caracteres < 2 or caracteres > 15:
                    print("La marca ingresada debe contener entre 2 y 15 caracteres!!")
                    marca=input("Ingrese marca del vehiculo: ")
                marca_almacenado=marca
                
            precio=int(input("Ingrese precio del vehículo: $ "))
            if precio >= 5000000:
                precio_almacenado=precio
            else: 
                print("El precio no es mayor a 5.000.000") 
            respuesta_multa=int(input("El vehiculo tiene multa?\n1.SI, \n2.NO: \n"))
            if respuesta_multa==1:
                multas=input("Ingrese el monto de la multa del vehículo: $ ")
                multas_almacenado=multas
                fecha_multas=input("Ingrese fecha de la multa del vehículo, siendo dd-mes-aaaa:  ")
                alma_fecha_multas=fecha_multas
            else:
                fecha_registro=input("Ingrese fecha de registro del vehículo: ")
            fecha_registro_almacenado=fecha_registro
            nombre_dueno=input("Ingrese nombre del dueño del vehículo: ")
            nombre_dueno_almacenado=nombre_dueno
            print()
        lista=[tipo_almacenado,patente_almacenado,marca_almacenado,precio_almacenado,multas_almacenado,alma_fecha_multas,fecha_registro_almacenado,nombre_dueno_almacenado]
        arreglo=np.array(lista)
        for i in range(1):
            print("El tipo de vehiculo ingresado fue un/a: ", tipo_almacenado)
            print("La patente vehicular ingresada fue: ", patente_almacenado)
            print("La marca del vehicular ingresada fue: ", marca_almacenado)
            if precio_almacenado>5000000:
                print("El precio del vehicular ingresado fue por un monto de: $", precio_almacenado)
            
            print("El valor de la multa ingresada del vehiculo fue: $", multas_almacenado)
            print("La fecha de la multa que tiene el vehiculo es del dd-mes-año: ", alma_fecha_multas)
            print("La fecha de registro vehicular fue el: ", fecha_registro_almacenado)
            print("El dueño del vehículo es: ", nombre_dueno_almacenado)

        continue
#SELECCION MENU 2 BUSCAR --------------------------------------------------------------------------------------------------------------
    if opcion == 2:
        print("Usted seleccionado opcion 2.- BUSCAR")
        buscar_patente=input("Ingrese patente del vehiculo a buscar: ")
        if buscar_patente == patente_almacenado:
            for i in range(1):
                print("El tipo de vehiculo ingresado fue un/a: ", tipo_almacenado)
                print("Su patente es: ", patente_almacenado)
                print("un vehiculo de marca: ", marca_almacenado)
                if precio_almacenado>5000000:
                    print("El precio del vehicular es de: $", precio_almacenado)
                print("El valor de la multa es de: $", multas_almacenado)
                print("Y su fecha es de (Ingrese bajo el siguiente formato dd-mes-año): ", alma_fecha_multas)
                print("La fecha de registro vehicular fue el: ", fecha_registro_almacenado)
                print("El dueño del vehículo es: ", nombre_dueno_almacenado)
        else:
            print("Patente no existe en sistema")
        continue
 #SELECCION MENU 3 -- CERTIFICADOS ------------------------------------------------------------------------------------------------   
    while certificado_act:
        if opcion == 3:
            print("Usted seleccionado opcion 3.- IMPRIMIR CERTIFICADOS")
            opcion_certificado=int(input("Que tipo de certificados desea?\n1.Emision de contaminantes\n2.Anotaciones Vigentes\n3.Certificado de Multas\nPresiones 1 opciones: "))
            for i in range(1):
                valor_aleatorio1=random.randint(1500,3500)
                valor_aleatorio2=random.randint(1500,3500)
                valor_aleatorio3=random.randint(1500,3500)
                if opcion_certificado == 1:
                    print("El valor de los ceritifcados de Emision de Contaminantes  tiene un costo de: $", valor_aleatorio1)
                if opcion_certificado == 2:
                    print("El valor de los ceritifcados de Anotaciones Vigentes, tiene un costo de: $", valor_aleatorio2)
                if opcion_certificado == 3:
                    print("El valor de los ceritifcados de Certificados de Multas, tiene un costo de: $", valor_aleatorio3)
                print("Los documentos impresos corresponden a la patente: ",patente_almacenado)
                print("Y su dueño es: ",nombre_dueno_almacenado)
            solicitar_certificado_adicional=int(input("Desea algun otro ceritifcado?\n1.SI\n2.NO\n"))
        if solicitar_certificado_adicional != 1:
            print("Selecciono la opcion no desear mas certificados, muchas gracias.")
            break
    
    if opcion == 4:
        print("Usted ha seleccionado la opcion 4.- SALIR")
        print("Gonzalo Cortez")
        print("Versión del Programa: 1.0")
        break

    #menu_act=False



        
        
            
                         


    