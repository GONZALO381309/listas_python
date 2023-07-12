menu_act=True
reserva_act=True

while menu_act:
    print("-.-.-.TE PASEO.-.-.-.-")
    print("")
    print("1. GRABAR")
    print("2. BUSCAR")
    print("3. iMPRIMIR BOLETA")
    print("4. SALIR")
    opcion=int(input("Ingrese una de las siguientes opciones de menú: "))
    if opcion == 1:
        print("Usted ha seleccionado la opcion: 1")
        fecha_reserva:input("Ingrese fecha de la reserva: ")
        hora_de_paseo=input("Ingrese la hora del paseo: ")
        Lugar_de_inicio_paseo=input("Ingrese el lugar de inicio del paseo: ")
        Lugar_de_fin_paseo=input("Ingrese lugar de finalización del paseo: ")
        mascotas_a_pasear=int(input("Ingrese cantidad de mascotas a pasear: "))
        nombre_persona_reserva=input("Ingrese el nombre de la persona que reserva: ")
        while reserva_act:
            num_reserva=int(input("Ingrese el numero de la reserva: "))
            if num_reserva >= 1000:
                print("Numero de la reserva fue ingresada correctamente")
                break
            else:
                print("Error, Reserva debe inciar desde el numero 1000")
        precio_de_la_paseada=input("Ingrese el precio de la paseada: ")
        print("Precio ha quedado guardado Correctamente")
        continue
      
    if opcion == 2:
        print("")
        continue

    if opcion == 3:
        print("")
        continue


    if opcion == 4:
        print("Usted ha seleccionado la opcion salir")
        print("Muchas gracias\nVuelva pronto.")
        break
        
    