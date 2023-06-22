import numpy as np

opcion_seleccionada=0
opcion=0
asiento=0
monto_asiento=12000
asiento_guardado=0
menu_act= True
while menu_act:
    print("----compra asientos cine---\n")
    print("1.SELECCION DE ASIENTOS")
    print("2.INGRESE DATOS PERSONALES PARA LA COMPRA DE ASIENTOS")
    print("3.SELECCION DE PELICULA")
    print("4.MOSTRAR BOLETA DE ASIENTOS")
    print("5.SALIR")
    opcion_seleccionada=int(input("Ingrese una opcion: "))

    if opcion_seleccionada < 1 or opcion_seleccionada > 6: 
        print ("error de seleccion")
    if opcion_seleccionada == 1:
        matrizasiento=np.empty((3,3),dtype=object)
        for a in range(3):
            for b in range(3):
                asiento = asiento + 1
                matrizasiento[a,b]=asiento
        print(matrizasiento)
        fila=int(input("Ingrese fila de asiento de su pasaje: "))
        if fila >= 0 or fila <= 3:
            fil=fila+1
        if fila < 0 or fila > 3:
            print("Fila fuera del rango, debe volver a ingresar")
            break
        columna=int(input("Ingrese columna de asiento de su pasaje: "))
        if columna >= 0 and columna <= 3:
            col=columna+1
        if columna < 0 or columna > 3:
            print("columna fuera del rango, debe volver a ingresar")
            break
        matrizasiento[fila,columna]="x"
        print(matrizasiento)
        print("seleccionate el asiento numero: ",fil*3-(3-col) )





        fila=int(input("Ingrese fila de asiento de su asiento: "))
        fil=fila+1
        columna=int(input("ingrese la columna de asiento: "))
        col=columna+1
        matrizasiento[fila,columna]="x"
        print(matrizasiento)
        print("seleccionate el asiento numero: ",fil*10-(10-col) ) 
   
    if opcion_seleccionada == 2:
        print("Usted ha seleciconado la opcion 2.INGRESE DATOS PERSONALES PARA COMPRA DE ASIENTO")
        nom_comprador=input("Ingrese nombre comprador: ")
        apellido_comprador=input("Ingrese apellido del comprador: ")
        rut_comprador1=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        correo_comprador=input("Ingrese correo del comprador: ")
        
        
        lista=["nom_comprador","apellido_comprador","rut_comprador","correo_comprador",fil*10-(10-col)]
        arreglo=np.array(len(lista))
        for i in range(1):
            print(f"El nombre y apellido ingresado fueron: {nom_comprador} - {apellido_comprador}")
            print("Y el Rut es: ", rut_comprador1)
            print(f"Señor/a {nom_comprador} se sienta en el {fil*10-(10-col)}")
            print("El correo para envío de información es: ", correo_comprador)
        continue 
    if opcion_seleccionada == 3:
        print("1.EL ARO")
        print("2.LA SIRENITA")
        print("3.THE FLASH")
        print("4.MARIO BROS")
        pelicula=int(input("seleccione una palicula: "))
        if pelicula==1:
            print("usted a seleccionado la pelicula EL ARO")
        if pelicula==2:
            print("usted a seleccionado la pelicula LA SIRENITA")
        if pelicula==3:
            print("usted a seleccionado la pelicula THE FLASH")
        if pelicula==4:
            print("usted a seleccionado la pelicula MARIO BROS")

    if opcion_seleccionada == 4:
        print("------------------BOLETA------------------")
        print(f"El total de la compra es de:-----$ {monto_asiento}")
        print("usuari@ vera:",(pelicula))
        print(f"El asiento comprado es el {fil*10-(10-col)}")
        #print("En el asiento numero: ",matrizbus)


    if opcion_seleccionada == 5:
        print("Usted selecciono la opcion 5. SALIR")
        print("Munchas gracias por su compra\nHasta luego.")
        break