opcion=0
opcion_info_vehi=0
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
    print("Ingreso información de vehículos:\n 1. Tipo \n 2. Patente \n 3. Marca \n 4. Precio \n 5. multas \n 6. Fecha Registro Vehículo \n 7. Nombre Dueño")
    opcion_info_vehi=int(input("Ingrese la informacion del vehiculo: "))
    if opcion_info_vehi == 1:
        tipo=input("Ingrese tipo de vehículo: ")
    if opcion_info_vehi == 2:
        patente=input("Ingrese patente vehicular: ")
    if opcion_info_vehi == 3:
        marca=input("Ingrese marca del vehiculo: ")
    if opcion_info_vehi == 4:
        precio=int(input("Ingrese precio del vehículo: "))
    if opcion_info_vehi == 5:
        multas=int(input("Ingrese el monto de la multa del vehículo: "))
    if opcion_info_vehi == 6:
        fecha_registro=input("Ingrese fecha de registro del vehículo: ")
    if opcion_info_vehi == 7:
        nombre_dueno=input("Ingrese nombre del dueño del vehículo: ")
