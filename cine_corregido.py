import numpy as np

opcion_seleccionada=0
opcion=0
asiento=0
monto_asiento=0
matrizasiento=[]
asiento_guardado=0
menu_act= True
asiento_act=True
lista_asiento=[]
opc=0

#INICIO FUNCIONES

def opc3():
    if opcion_seleccionada == 3:
        print("1.EL ARO")
        print("2.LA SIRENITA")
        print("3.THE FLASH")
        print("4.MARIO BROS")
        ingreso_pelicula=int(input("seleccione una palicula: "))
        if ingreso_pelicula==1:
            ingreso_pelicula="EL ARO"
            print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        if ingreso_pelicula==2:
            ingreso_pelicula="LA SIRENITA"
            print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        if ingreso_pelicula==3:
            ingreso_pelicula="THE FLASH"
            print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        if ingreso_pelicula==4:
            ingreso_pelicula="MARIO BROS"
            print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        #return ingreso_pelicula

def opc4():
    if opcion_seleccionada == 4:
        ingreso_pelicula=0
        print("------------------------------------------")
        print("-----    >>>>>> BOLETA <<<<<<    ---------")
        print("------------------------------------------")
        print(f"El total de la compra es de:-----$ {monto_asiento}")
        print("Usuari@ verá la pelicula: ", ingreso_pelicula)
        print(f"El asiento comprado es o son los Nª {lista_asiento}")
      
#FIN FUNCIONES

#############################################     INGRESO MENU OPCION 1    #############################################################
while menu_act:
    print("------------------------------")
    print("----MENU DE INGRESO AL CINE---")
    print("------------------------------")
    print("1.SELECCION DE ASIENTOS")
    print("2.INGRESE DATOS PERSONALES PARA LA COMPRA DE ASIENTOS")
    print("3.SELECCION DE PELICULA")
    print("4.MOSTRAR BOLETA DE ASIENTOS")
    print("5.SALIR")
    opcion_seleccionada=int(input("Ingrese una opcion: "))
    if opcion_seleccionada < 1 or opcion_seleccionada >= 6: 
        print ("error de seleccion")
    else:
        if opcion_seleccionada == 1:
            print("Usted a seleccionado la opcion 1 - SELECCION DE ASIENTOS")
            matrizasiento=np.empty((3,3), dtype=(object))
            for fila in range(3):
                for columna in range (3):
                    asiento=asiento+1
                    matrizasiento[fila,columna]=asiento
            print(matrizasiento)
            while True:
                try:
                    fila=int(input("Ingrese fila de asiento a seleccionar: "))
                    if fila >=0 or fila <=3:
                        fil=fila+1
                        break
                except:
                    print("Sólo debe ingresar numeros!!")
            while True:   
                try:
                    columna=int(input("Ingrese columna de asiento a seleecionar: "))
                    if columna >=0 or columna <=3:
                        col=columna+1
                        break
                except:
                    print("Sólo debe ingresar numeros!!")
            li=fil*3-(3-col)
            lista_asiento.append(li)
            matrizasiento[fila,columna]="x"
            print(matrizasiento)
            print("seleccionate el asiento numero: ",fil*3-(3-col))
            while True:
                opc=int(input("desea seleccionar otro asiento: \n1.SI\n2.NO\n "))
                if opc==1:
                    fila=int(input("Ingrese fila de asiento a seleccionar: "))
                    if fila >=0 or fila <=3:
                        fil=fila+1
                    columna=int(input("Ingrese columna de asiento a seleccionar: "))
                    if columna >=0 or fila <=3:
                        col=columna+1
                    matrizasiento[fila,columna]="x"
                print(matrizasiento)
                print("seleccionate el asiento numero: ",fil*3-(3-col) )
                lista_asiento.append(fil*3-(3-col))
               
                if opc==2:
                    break
##########################################     INGRESO MENU 2   ############################################################333
        if opcion_seleccionada == 2:
            print("Usted a ingresado a la opcion 2.INGRESE DATOS PERSONALES PARA LA COMPRA DE ASIENTOS")
            nom_comprador=input("Ingrese nombre de la persona titular: ")
            while True:
                try:
                    run_comprador=int(input("Ingrese Run de la persona (Sólo numeros, sin puntos ni guión): "))
                    if run_comprador > 3000000 and run_comprador <= 99999999:
                        print("Run ingresado correctamente!!")
                        break
                    else:
                        print("El numero de Run debe ser entre 3000000 y 99999999")  
                except:
                    print("Error---> El Ingreso de Run debe ser sólo numerico") 
                    print("")

##########################################      INGRESO MENU OPCION 4 PARA MOSTRAR BOLETA DE ASIENTOS     ################################################
        if opcion_seleccionada == 4:
            opc4()


##########################################      INGRESO MENU OPCION 5 PARA SALIR     ################################################

        if opcion_seleccionada == 5:
            print("Usted a seleccionado la opcion 5. SALIR")
            print("Muchas gracias por venir")
            print("Hasta Luego!!.")
            break 