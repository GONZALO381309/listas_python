import numpy as np
import random
menu_act=True
reserva_act=True
mascota_act=True
buscar_activo=True
seleccion_act=True
fecha_reserva=""
hora_de_paseo=""
Lugar_de_inicio_paseo=""
Lugar_de_fin_paseo=""
mascotas_a_pasear=0
nombre_persona_reserva=""
num_reserva=0
precio_de_la_paseada=0

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
        lista=["acumulador_fecha","acumulador_hora","acumulador_inicio","acumulador_fin","acumulador_mascotas","acumulador_persona","acumulador_reserva","acumulador_precio"]
        arreglo=np.array(lista)
        for i in range(1):
            print("La fecha de paseo es: ", acumulador_fecha)
            print("La hora de paseo es: ", acumulador_hora)
            print("El inicio del paseo comienza en: ", acumulador_inicio)
            print("El termino del paseo finaliza en: ", acumulador_fin)
            print("La cantidad de mascotas a pasear es/son: ", acumulador_mascotas)
            print("La persona que agendo el servicio es Don/Señora: ", acumulador_persona)
            print("El numero de la reserva es: ", acumulador_reserva)
            print("El precio por el servicio de paseo es de: $ ", acumulador_precio)
        
            continue
##############################################################################################################     BUSCAR     
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
                        print("")
                        if nombre_persona_reserva == acumulador_persona:
                            print("La fecha de paseo es: ", acumulador_fecha)
                            print("La hora de paseo es: ", acumulador_hora)
                            print("El inicio del paseo comienza en: ", acumulador_inicio)
                            print("El termino del paseo finaliza en: ", acumulador_fin)
                            print("La cantidad de mascotas a pasear es/son: ", acumulador_mascotas)
                            print("La persona que agendo el servicio es Don/Señora: ", acumulador_persona)
                            print("El numero de la reserva es: ", acumulador_reserva)
                            print("El precio por el servicio de paseo es de: $ ", acumulador_precio)
                            break
                        else:
                            print("Verificando, por favor espere...........")
                            print("No existe el nombre de la persona a buscar en la base de datos")
                            continue
                    if op == 2:
                        num_reserva=int(input("Ingrese numero de reserva: "))
                        print("")
                        if num_reserva == acumulador_reserva:
                            print("La fecha de paseo es: ", acumulador_fecha)
                            print("La hora de paseo es: ", acumulador_hora)
                            print("El inicio del paseo comienza en: ", acumulador_inicio)
                            print("El termino del paseo finaliza en: ", acumulador_fin)
                            print("La cantidad de mascotas a pasear es/son: ", acumulador_mascotas)
                            print("La persona que agendo el servicio es Don/Señora: ", acumulador_persona)
                            print("El numero de la reserva es: ", acumulador_reserva)
                            print("El precio por el servicio de paseo es de: $ ", acumulador_precio)
                            break
                        else:
                             print("Verificando, por favor espere...........")
                             print("No existe el numero de reserva a buscar en la base de datos")
                            
            except:
                    break
                
        continue
    print("")

 #################################################################################################          IMPRIMIR BOLETA   
    if opcion == 3:
        costo_aleatorio=random.randint(3500,12900)
        print("-----------------       BOLETA       -----------------")
        print("")
        print("La fecha del viaje a cobrar, fue le día: ", acumulador_fecha)
        print("La cantidad de mascotas a pasear fue/fueron: ", acumulador_mascotas)
        print("-----------------------------------------------------")
        print("El total del precio del paseo es: ", costo_aleatorio)
        print("El total de mascotas a pasear es: ", acumulador_mascotas)
        print("El costo por paseo es de: ",acumulador_precio)
        print("******************************************************")
        
        print(f"El total a cancelar es: ")
        usuario="Gonzalo"
        clave=12
        while seleccion_act:
            seleccion_tarjeta=int(input("Como desea cancelar?\n1.TARJETA DEBITO\n2.TARJETA CREDITO\n3.EFECTIVO\n4.CANCELAR\nSeleccion una opcion:"))

    #################################################################################################             TARJETA DE DEBITO         
            
            if seleccion_tarjeta == 1:
                print("Deslice tarjeta de debito")
                print("Leyendo tarjeta debito......por favor espere..")
                ingreso_usuario=input("Ingrese nombre de usuario: ")
                ingreso_clave=int(input("Ingrese clave de acceso: "))
                if ingreso_usuario != usuario and ingreso_clave != 12:
                    print("Error--- Usuario o clave de acceso no son correctos")
                else:
                    print("Usted ha ingresado correctamente")
                    print(f"El monto a cancelar es: {costo_aleatorio}")
                    opc=int(input("Por favor confirme el monto\n1.SI\n2.NO\nSeleccion: "))
                    if opc == 1:
                        print("Pago aceptado correctamente\nMuchas gracias por su compra\nHasta Luego")
                        break
                    else:
                        print("Pago no aceptado!! - verifique e informe a cordinador")
                        continue 

################################################################################################                     TARJETA DE CREDITO
  
            if seleccion_tarjeta == 2:
                print("Deslice tarjeta de credito")
                print("Leyendo tarjeta credito......por favor espere..")
                ingreso_usuario=input("Ingrese nombre de usuario: ")
                ingreso_clave=int(input("Ingrese clave de acceso: "))
                if ingreso_usuario != usuario and ingreso_clave != 12:
                    print("Error--- Usuario o clave de acceso no son correctos")
                else:
                    print("Usted ha ingresado correctamente")
                    print("")
                    seleccion_cuota=int(input("Desea con cuotas o sin cuotas?\n1.SIN CUOTAS\n2.CON CUOTAS\nSeleccion: "))
                    if seleccion_cuota == 1:
                        sin_cuota=int(input("Selecciono sin cuotas\nPresiones 1.Para validar pago\n2.Para Salir\nSeleccion: "))
                        if sin_cuota == 1:
                            print("Pago aceptado correctamente\nMuchas gracias por su compra\nHasta Luego")
                            break
                        if sin_cuota == 2:
                            print("Usted ha cancelado la operación.. Gracias")
                            break
                    if seleccion_cuota == 2:
                        cuota=int(input("Ingrese cantidad de cuotas\n1. 1 CUOTA\n2. 3 CUOTAS\n3. 6 CUOTAS\nSeleccion: "))
                        try:
                            if cuota == 1:
                                print(f"El valor a cancelar es {costo_aleatorio}")
                                print("Pago aceptado correctamente\nMuchas gracias por su compra\nHasta Luego")
                                break
                            elif cuota == 2:
                                print("Cada persona debe cancelar un monto de: $" , costo_aleatorio / 3)
                                break
                            elif cuota == 3:
                                print("Cada persona debe cancelar un monto de: $" , costo_aleatorio / 6)
                                break
                            else:
                                print("Debe seleccionar una de las 3 opciones de cuotas")

                        except:
                                print("")

###########################################################################################         CANCELAR EN EFECTIVO             
            
            if seleccion_tarjeta == 3:
                print("Sólo acreque a la caja y cancele el monto de $ ", costo_aleatorio)
                print("Pago recibido por caja\nMuchas gracias por su compra\nHasta Luego")

###############################################################################################    CANCELAR COMPRA

            if seleccion_tarjeta == 4:
                print("Usted ha cancelado su compra\nMuchas gracias\nHasta Luego")
           
        continue

###############################################################################################     SALIR DEL SISTEMA
    if opcion == 4:
        print("Usted ha seleccionado la opcion salir")
        print("Muchas gracias\nVuelva pronto.")
        break
        
    