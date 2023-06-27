import numpy as np
#from compra_de_pasaje_funciones import *
monto_pasaje=0
asiento=0
seleccion_pasaje_act=True
menu_act=True
bucle=True
opcion=0
matrizbus1=0
rut_comprador1=0
asiento_guardado=0
lista_asiento=[]

#CREACION MENU
while menu_act:
    print("-------------------------------------")
    print("----MENU COMPRA DE PASAJES DE BUS----")
    print("-------------------------------------")
    print()
    print("1.INGRESE COMPRA DE PASAJES")
    print("2.INGRESE DATOS PERSONALES PARA COMPRA DE PASAJES")
    print("3.INGRESE NUMERO DE ASIENTO A COMPRAR")
    print("4.BUSCAR PASAJE")
    print("5.MOSTRAR BOLETA DE PASAJE")
    print("6.SALIR")
    opcion_seleccionada=int(input("Ingrese una opcion: "))

    if opcion_seleccionada < 1 or opcion_seleccionada > 6:
        print("Opcion ingresada no valida!")
    
    if opcion_seleccionada == 1:
        print("Usted ha seleciconado la opcion 1.INGRESE COMPRA DE PASAJES")
        ingreso_destino=int(input("Seleccione Donde viaja?\n1.Puerto Montt $5.000\n2.Santiago $29.000\n3.Puerto Varas $5000\n4.Valdivia $6.500\n5.Osorno $2.500:\nOpcion: "))
        cantidad_pasaje=int(input("Ingrese cuantos pasajes desea: "))
        if ingreso_destino == 1: 
            total_compra_pasaje=5000*cantidad_pasaje
        elif ingreso_destino == 2:
            total_compra_pasaje=29000*cantidad_pasaje
        elif ingreso_destino == 3:
            total_compra_pasaje=5000*cantidad_pasaje
        elif ingreso_destino == 4:
            total_compra_pasaje=6500*cantidad_pasaje
        elif ingreso_destino == 5:
            total_compra_pasaje=2500*cantidad_pasaje
        print("El valor a cancelar por la compra de pasaje es: $", total_compra_pasaje)

#OPCION 2 DEL MENU---- INGRESO DE DATOS DEL COMPRADOR------------------------------------------------------------------------         
    if opcion_seleccionada == 2:
        print("Usted ha seleciconado la opcion 2.INGRESE DATOS PERSONALES PARA COMPRA DE PASAJES")
        nom_comprador=input("Ingrese nombre comprador: ")
        apellido_comprador=input("Ingrese apellido del comprador: ")
        rut_comprador1=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        correo_comprador=input("Ingrese correo para envio de copia de pasaje: ")
        Destino=input("Ingrese el destino: ")
        print()
        lista=["nom_comprador","apellido_comprador","rut_comprador","correo_comprador","Destino"]
        arreglo=np.array(len(lista))
        for i in range(1):
            print(f"El nombre y apellido ingresado fueron: {nom_comprador} - {apellido_comprador}")
            print("Y el Rut es: ", rut_comprador1)
            print(f"Señor/a {nom_comprador} viaja a {Destino}")
            print("El correo para envío de copia pasajes es: ", correo_comprador)
        continue
            
#OPCION SELECCION DE ASIENTOS   ------------------------------------------------------------------------------
   
    if opcion_seleccionada == 3:
        print("Usted ha seleciconado la opcion 3.INGRESE NUMERO DE ASIENTO A COMPRAR")
        matrizbus=np.empty((10,4),dtype=object)
        for a in range(10):
            for b in range(4):
                asiento = asiento + 1
                matrizbus[a,b]=asiento
        print(matrizbus)
        fila=int(input("Ingrese fila de asiento de su pasaje: "))
        if fila >= 0 or fila <= 10:
            fil=fila+1
        if fila < 0 or fila > 10:
            print("Fila fuera del rango, debe volver a ingresar")
        
        columna=int(input("Ingrese columna de asiento de su pasaje: "))
        if columna >= 0 and columna <= 4:
            col=columna+1
        if columna < 0 or columna > 4:
            print("columna fuera del rango, debe volver a ingresar")
        
            break
        li=fil*4-(4-col)
        lista_asiento.append(li)
        matrizbus[fila,columna]="x"
        print(matrizbus)
        print("seleccionaste el asiento numero: ",fil*4-(4-col) )

        while seleccion_pasaje_act:
            opcion=int(input("desea seleccionar otro asiento: \n1.SI\n2.NO\n "))
            if opcion==1 :
                fila=int(input("Ingrese fila de asiento de su pasaje: "))
                
                if fila >= 0 or fila <= 10:
                    fil=fila+1
                if fila < 0 or fila > 10:
                    print("Fila fuera del rango, debe volver a ingresar")
                    break
                columna=int(input("Ingrese columna de asiento de su pasaje: "))
                
                if columna >= 0 and columna <= 4:
                    col=columna+1
                if columna < 0 or columna > 4:
                    print("columna fuera del rango, debe volver a ingresar")
                    break
                
                matrizbus[fila,columna]="x"
                print(matrizbus)
                print("seleccionate el asiento numero: ",fil*4-(4-col) )
                lista_asiento.append(fil*4-(4-col))
                continue
            if opcion==2:
                break  

 #OPCION DE BUSQUEDA DE PASAJE -------------------------------------------------------------------------------------------           

    if opcion_seleccionada == 4:
        
        print("Usted ha seleciconado la opcion 4.BUSCAR PASAJE")
        rut_comprador=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        if rut_comprador == rut_comprador1:
            print(f"El nombre y apellido ingresado es: {nom_comprador}  {apellido_comprador}")
            print("Y el Rut es: ", rut_comprador1)
            print("El correo para envío de pasajes es: ", correo_comprador)
            print("Y viaja a ", Destino)
            print("En el/os asientos Nº: ", lista_asiento)

        else:
            print("Rut no existe o fue ingresado erroneamente")
        
#OPCION DE VER BOLETA CON DETALLE ------------------------------------------------------------------------------------

    if opcion_seleccionada == 5:
        print("------------------BOLETA------------------")
        print(f"El total de la compra es de:-----$ {total_compra_pasaje}")
        print(f"Señor/a {nom_comprador} viaja a {Destino}")
        print(f"En el/os asiento/s Nº: ",lista_asiento)
        
        
 #OPCION DE SALIDA DEL SISTEMA  ---------------------------------------------------------------------------------------
  
    if opcion_seleccionada == 6:
        print("Usted ha seleciconado la opcion 6.SALIR")
        print("Gracias por preferirnos,\nHasta luego")
        break


