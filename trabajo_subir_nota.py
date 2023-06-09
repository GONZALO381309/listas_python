#VARIABLES DE INFORMACION DE INFORMACION VEHICULO
marca=(2,15)
#----------------------------------------------------
opcion=0
opcion_info_vehi=0
lista=()
#ALMACENAMIENTO DE INFORMACION VEHICULAR
tipo_almacenado=0
patente_almacenado=0
marca_almacenado=0
precio_almacenado=0
multas_almacenado=0
fecha_registro_almacenado=0
nombre_dueno_almacenado=0
print("Bienvenido a la Automotora AUTO SEGURO")
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
        patente_almacenado=patente
        marca=input("Ingrese marca del vehiculo: ")
        if marca < "2" or marca > "15":
            print("ERROR----> Sólo debe ingresar minimo de 2 a 15 caracteres")
            break
        marca_almacenado=marca
        precio=int(input("Ingrese precio del vehículo: "))
        precio_almacenado=precio
        multas=int(input("Ingrese el monto de la multa del vehículo: "))
        multas_almacenado=multas
        fecha_registro=input("Ingrese fecha de registro del vehículo: ")
        fecha_registro_almacenado=fecha_registro
        nombre_dueno=input("Ingrese nombre del dueño del vehículo: ")
        nombre_dueno_almacenado=nombre_dueno
    lista= tipo_almacenado,patente_almacenado,marca_almacenado,precio_almacenado,multas_almacenado,fecha_registro_almacenado,nombre_dueno_almacenado
    print("Los datos almacenados en informacion vehicular son: ", lista)
    