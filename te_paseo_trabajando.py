import numpy as np
menu_act=True
reserva_act=True
mascota_act=True
buscar_activo=True
fecha_reserva=""
hora_de_paseo=""
Lugar_de_inicio_paseo=""
Lugar_de_fin_paseo=""
mascotas_a_pasear=0
nombre_persona_reserva=""
num_reserva=0
precio_de_la_paseada=0
lista=[]
while menu_act:
    print("-.-.-.TE PASEO.-.-.-.-")
    print("")
    print("1. GRABAR")
    print("2. BUSCAR")
    print("3. IMPRIMIR BOLETA")
    print("4. SALIR")
    opcion=int(input("Ingrese una de las siguientes opciones de menú: "))
    if opcion == 1:
        print("Usted ha seleccionado la opcion: 1")
        fecha_reserva:input("Ingrese fecha de la reserva: ")
        acumulador_fecha=fecha_reserva
        hora_de_paseo=input("Ingrese la hora del paseo: ")
        acumulador_hora=hora_de_paseo
        Lugar_de_inicio_paseo=input("Ingrese el lugar de inicio del paseo: ")
        acumulador_inicio=Lugar_de_inicio_paseo
        Lugar_de_fin_paseo=input("Ingrese lugar de finalización del paseo: ")
        acumulador_fin=Lugar_de_fin_paseo
        while mascota_act:
            mascotas_a_pasear=int(input("Ingrese cantidad de mascotas a pasear: "))
            acumulador_mascotas=mascotas_a_pasear
            if mascotas_a_pasear < 1 or mascotas_a_pasear > 5:
                print("Solo debe ingresar mascotas entre 1 y 5")
            else:
                print("Cantidad de mascotas ingresadas al sistema")
                break
        nombre_persona_reserva=input("Ingrese el nombre de la persona que reserva: ")
        acumulador_persona=nombre_persona_reserva
        while reserva_act:
            num_reserva=int(input("Ingrese el numero de la reserva: "))
            acumulador_reserva=num_reserva
            if num_reserva >= 1000:
                print("Numero de la reserva fue ingresada correctamente")
                break
            else:
                print("Error, Reserva debe inciar desde el numero 1000")
        precio_de_la_paseada=input("Ingrese el precio de la paseada: ")
        acumulador_precio=precio_de_la_paseada
        print("Precio ha quedado guardado Correctamente")
        print("")
        lista=[acumulador_fecha,acumulador_hora,acumulador_inicio,acumulador_fin,acumulador_mascotas,acumulador_persona,acumulador_reserva,acumulador_precio]
        
        print("La fecha de paseo es: ", acumulador_fecha)
        print("La hora de paseo es: ", acumulador_hora)
        print("El inicio del paseo comienza en: ", acumulador_inicio)
        print("El termino del paseo finaliza en: ", acumulador_fin)
        print("La cantidad de mascotas a pasear es/son: ", acumulador_mascotas)
        print("La persona que agendo el servicio es Don/Señora: ", acumulador_persona)
        print("El numero de la reserva es: ", acumulador_reserva)
        print("El precio por el servicio de paseo es de: $ ", acumulador_precio)
            
        continue
      
    if opcion == 2:
        print("Usted a seleccionado la opcion 2.- BUSCAR")
        while buscar_activo:
            op=int(input("Ingrese opcion a buscar\n1.Por nombre\n2.Por numero de reserva\nseleccion: "))
            try:
                if op < 1 or op > 2:
                    print("Debe ingresar solo opcion 1 o 2")
                else:
                    if op == 1:
                        nombre_persona_reserva=input("Ingrese el nombre de la persona a buscar: ")
                        print("Verificando, por favor espere...........")
                        
                        if nombre_persona_reserva < 1:
                            print("Debe ingresar al menos un caracter")
                        else:
                            continue
                    if op == 2:
                        num_reserva=int(input("Ingrese numero de reserva: "))
                        print("Verificando, por favor espere...........")
                        
                        if num_reserva != acumulador_reserva:
                            print("No existe numero de reserva, favor verifique")
                        else:
                            continue
            except:
                break
                
        continue

    if opcion == 3:
        print("")
        continue


    if opcion == 4:
        print("Usted ha seleccionado la opcion salir")
        print("Muchas gracias\nVuelva pronto.")
        break
        
    