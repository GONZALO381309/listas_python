user="hmayorga"
password=1234
user2="Gcortez"
paswword_usuer2=12
menu_activo=True
opcion=0
validador_ingreso_menu=True
num_persona=0
#INFORMACION DE IMPRESIONES
tipo_impresiones=0
cantidad_impresiones_bn=0
total_cantidad_impre_bn=0
acumulador_impresion_bn=0
cantidad_impresiones_color=0
total_cantidad_impre_color=0
acumulador_impresion_color=0
#INFORMACION FOTOCOPIAS
cantidad_fotocopias=0
total_fotocopias=0
acumulador_fotocopia=0
#INFORMACION ANILLADOS
cantidad_anillados=0
total_anillados=0
acumulador_anillado=0
#SELECCION DESCUENTO
selec_desc1=0
resp_desc_diurno=0

print("Bienvenido al sistema de fotocopiado de DUOC UC")
usuario=input("Si es alumno regular de DUOC UC ingrese usuario: ")
contraseña=int(input("Ingrese contraseña: "))
if usuario == user and contraseña == 1234 or usuario == user2 and contraseña == 12:
    print("Bienvenido al menu")
    print()
    while menu_activo:
        print("----MENU----")
        print("")
        print("Elija una de las siguientes opciones:\n1.- IMPRESION\n2.- FOTOCOPIAS\n3.- ANILLADOS\n4.- PAGAR\n5.- ANULAR SERVICIO\n6.- SALIR DEL SISTEMA")
        opcion=int(input("Ingrese una opcion: "))
        if opcion < 1 or opcion > 6:
            print("Debe ingresar una opcion valida")
        if opcion == 1:
            print("Usted a seleccionado la opcion 1.IMPRESION")
            tipo_impresiones=int(input("¿Que tipo de impresiones desea?\n1.BN $150\n2.COLOR $300\n: "))
            if tipo_impresiones == 1:
                print("Usted a seleccionado impresion BN $150 ¿Cuantas impresiones desea?")
                cantidad_impresiones_bn=int(input(""))
                total_cantidad_impre_bn=150*cantidad_impresiones_bn
                acumulador_impresion_bn=acumulador_impresion_bn + total_cantidad_impre_bn
                print(f"Usted lleva hasta el momento un monto a cancelar de ${acumulador_impresion_bn} impresiones en BN")
            if tipo_impresiones == 2:
                print("Usted a seleccionado impresion COLOR $300 ¿Cuantas impresiones desea?")
                cantidad_impresiones_color=int(input(""))
                total_cantidad_impre_color=300*cantidad_impresiones_color
                acumulador_impresion_color=acumulador_impresion_color + total_cantidad_impre_color
                print(f"Usted lleva hasta el momento un monto a cancelar de ${acumulador_impresion_color} impresiones a color")
            total_impre_acumulada=acumulador_impresion_bn + acumulador_impresion_color
            print("Subtotal a cancelar por impresiones BN y Color $", total_impre_acumulada)

        if opcion == 2:
            print("Usted a seleccionado la opcion 3.FOTOCOPIAS $80")
            cantidad_fotocopias=int(input("Ingrese la cantidad de fotocopias que necesita: "))
            total_fotocopias=80*cantidad_fotocopias
            acumulador_fotocopia=acumulador_fotocopia + total_fotocopias
            print(f"Usted lleva hasta el momento un monto a cancelar de ${acumulador_fotocopia} fotocopias")

        if opcion == 3:
            print("Usted a seleccionado la opcion 3.ANILLADOS $5000")
            cantidad_anillados=int(input("Ingrese la cantidad de anillados que necesita: "))
            total_anillados=5000*cantidad_anillados
            acumulador_anillado=acumulador_anillado + total_anillados

            print(f"Usted lleva hasta el momento un monto a cancelar de ${acumulador_anillado} anillados")

        if opcion == 4:
            print("Desgloce por tipo de servicio seleccionado:")
            print("Total por impresiones en BN $",acumulador_impresion_bn)
            print("Total por impresiones a COLOR $",acumulador_impresion_color)
            print("Total por fotocopias $",acumulador_fotocopia)
            print("Total por anillados $",acumulador_anillado)
            total_general=acumulador_impresion_bn + acumulador_impresion_color + acumulador_fotocopia + acumulador_anillado
            print("El total a cancelar es de: $",total_general)
            print("Es alumno DIURNO - VESPERTINO O ADMINISTRATIVO? \n1.DIURNO \n2.VESPERTINO \n3.ADMINISTRATIVO")
            selec_desc1=int(input(""))
            if selec_desc1 == 1:
                print("Usted tiene un 10 por ciento de descuento: ")
                print("Debe cancelar: ",total_general*0.90)
                total_descuento= total_general*0.90
                print("Indique entre cuantas personas va a cancelar")
                num_persona=int(input())
                if num_persona == 1:
                    print("Usted debe cancelar: $",total_descuento)
                if num_persona > 1:
                    print("Cada persona debe cancelar:$",total_descuento/num_persona)
            if selec_desc1 == 2:
                print("Usted tiene un 20 por ciento de descuento: ")
                print("Debe cancelar: ",total_general*0.80)
                total_descuento2= total_general*0.80
                print("Indique entre cuantas personas va a cancelar")
                num_persona=int(input())
                if num_persona == 1:
                    print("Usted debe cancelar: $",total_descuento2)
                if num_persona > 1:
                    print("Cada persona debe cancelar:$",total_descuento2/num_persona)
            if selec_desc1 == 3:
                print("Usted no tiene descuento: ")
                print("Debe cancelar: $",total_general)
                print("Indique entre cuantas personas va a cancelar")
                num_persona=int(input())
                if num_persona == 1:
                    print("Usted debe cancelar: $",total_general)
                if num_persona > 1:
                    print("Cada persona debe cancelar:$",total_general/num_persona)
            print("Gracias por su compra")

        if opcion == 5:
            num_persona=0
            #INFORMACION DE IMPRESIONES
            tipo_impresiones=0
            cantidad_impresiones_bn=0
            total_cantidad_impre_bn=0
            acumulador_impresion_bn=0
            cantidad_impresiones_color=0
            total_cantidad_impre_color=0
            acumulador_impresion_color=0
            #INFORMACION FOTOCOPIAS
            cantidad_fotocopias=0
            total_fotocopias=0
            acumulador_fotocopia=0
            #INFORMACION ANILLADOS
            cantidad_anillados=0
            total_anillados=0
            acumulador_anillado=0
            #SELECCION DESCUENTO
            selec_desc1=0
            resp_desc_diurno=0

        if opcion == 6:
            print("Usted a seleccionado opcion 6.- SALIR")
            print("Ha salido del sistema, muchas gracias")
            break
    
    
    
    
    
    
    menu_activo=False

else:
    usuario=input("Vuelva a ingresar usuario: ")
    contraseña=int(input("Ingrese contraseña: "))


        
    
