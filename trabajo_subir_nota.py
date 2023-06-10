import numpy as np
#VARIABLES DE INFORMACION DE INFORMACION VEHICULO
marca=(2,15)
#----------------------------------------------------
opcion=0
opcion_info_vehi=0
lista=()
multas=0
menu_act=True
#ALMACENAMIENTO DE INFORMACION VEHICULAR
tipo_almacenado=0
patente_almacenado=0
marca_almacenado=0
precio_almacenado=0
multas_almacenado=0
fecha_registro_almacenado=0
nombre_dueno_almacenado=0
print("Bienvenido a la Automotora AUTO SEGURO")
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
            marca_almacenado=marca
            precio=int(input("Ingrese precio del vehículo: $ "))
            if precio >= 5000000:
                precio_almacenado=precio
            else: 
                print("El precio no es mayor a 5.000.000") 
            respuesta_multa=int(input("El vehiculo tiene multa?\n1.SI, \n2.NO: \n"))
            if respuesta_multa==1:
                multas=input("Ingrese el monto de la multa del vehículo: ")
            else:
                multas_almacenado=multas
            fecha_registro=input("Ingrese fecha de registro del vehículo: ")
            fecha_registro_almacenado=fecha_registro
            nombre_dueno=input("Ingrese nombre del dueño del vehículo: ")
            nombre_dueno_almacenado=nombre_dueno
        lista= tipo_almacenado,patente_almacenado,marca_almacenado,precio_almacenado,multas_almacenado,fecha_registro_almacenado,nombre_dueno_almacenado
        print("Los datos almacenados en informacion vehicular son: ", lista)

    if opcion == 2:
        print("Usted seleccionado opcion 2.- BUSCAR")
        buscar_patente=input("Ingrese patente del vehiculo a buscar: ")
        if buscar_patente == patente_almacenado:
            print(lista)
        break
    