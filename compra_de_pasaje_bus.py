import numpy as np

asiento=0
seleccion_pasaje_act=True
menu_act=True
matrizbus1=0
rut_comprador1=0
#CREACION MENU
while menu_act:
    print("----MENU COMPRA DE PASAJES DE BUS---\n")
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
        monto_pasaje=input("Ingrese valor del pasaje: ")
         
    if opcion_seleccionada == 2:
        print("Usted ha seleciconado la opcion 2.INGRESE DATOS PERSONALES PARA COMPRA DE PASAJES")
        nom_comprador=input("Ingrese nombre comprador: ")
        apellido_comprador=input("Ingrese apellido del comprador: ")
        rut_comprador1=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        correo_comprador=input("Ingrese correo del comprador: ")
        Destino=input("Ingrese el destino: ")
        print()
        lista=["nom_comprador","apellido_comprador","rut_comprador","correo_comprador","Destino"]
        arreglo=np.array(len(lista))
        for i in range(1):
            print(f"El nombre y apellido ingresado fueron: {nom_comprador} - {apellido_comprador}")
            print("Y el Rut es: ", rut_comprador1)
            print(f"Señor/a {nom_comprador} viaja a {Destino}")
            print("El correo para envío de información es: ", correo_comprador)
        continue
            

   
    if opcion_seleccionada == 3:
        print("Usted ha seleciconado la opcion 3.INGRESE NUMERO DE ASIENTO A COMPRAR")
        matrizbus=np.empty((10,4),dtype=object)
        for a in range(10):
            for b in range(4):
                asiento = asiento + 1
                matrizbus[a,b]=asiento
        print(matrizbus)

        while seleccion_pasaje_act:
            fila=int(input("Ingrese fila de asiento de su pasaje: "))
            if fila < 0 or fila > 10:
                print("Fila fuera del rango, debe volver a ingresar")
                break
            columna=int(input("Ingrese columna de asiento de su pasaje: "))
            if columna < 0 or columna > 4:
                print("columna fuera del rango, debe volver a ingresar")
                break
            matrizbus[fila,columna]="X"
            print(matrizbus)
           

    if opcion_seleccionada == 4:
        print("Usted ha seleciconado la opcion 4.BUSCAR PASAJE")
        rut_comprador=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        if rut_comprador == rut_comprador1:
           print(f"El nombre y apellido ingresado fueron: {nom_comprador} - {apellido_comprador}")
           print("Y el Rut es: ", rut_comprador1)
           print("El correo para envío de información es: ", correo_comprador)
           print("Y viaja a ", Destino)
        else:
            print("Rut no existe o fue ingresado erroneamente")
        

    if opcion_seleccionada == 5:
        print("------------------BOLETA------------------")
        print(f"El total de la compra es de:-----$ {monto_pasaje}")
        print(f"Señor/a {nom_comprador} viaja a {Destino}")
        #print("En el asiento numero: ",matrizbus)


    if opcion_seleccionada == 6:
        print("Usted ha seleciconado la opcion 6.SALIR")
        print("Gracias por preferirnos,\nHasta luego")
        break

