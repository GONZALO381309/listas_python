import numpy as np

opcion_seleccionada=0
opcion=0
asiento=0
monto_asiento=12000
matrizasiento=0
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
    
    if opcion_seleccionada < 1 or opcion_seleccionada > 6: 
            print ("error de seleccion")
    else:
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
            if columna >= 0 or columna <= 3:
                col=columna+1
            if columna < 0 or columna > 3:
                print("columna fuera del rango, debe volver a ingresar")
                break
            li=fil*3-(3-col)
            lista_asiento.append(li)
            matrizasiento[fila,columna]="x"
            print(matrizasiento)
            print("seleccionate el asiento numero: ",fil*3-(3-col))
        
      
            opc=int(input("desea seleccionar otro asiento: \n1.SI\n2.NO\n "))
        while asiento_act: 
            if opc==1:
                fila=int(input("Ingrese fila de asiento de su pasaje: "))
                if fila >= 0 or fila <= 10:
                    fil=fila+1
                else:
                    print("Fila fuera del rango, debe volver a ingresar")
                    break
                columna=int(input("Ingrese columna de asiento de su pasaje: "))
                if columna >= 0 and columna <= 4:
                    col=columna+1
                else:
                    print("columna fuera del rango, debe volver a ingresar")
                    break
        
                matrizasiento[fila,columna]="x"
                print(matrizasiento)
                print("seleccionate el asiento numero: ",fil*3-(3-col) )
                lista_asiento.append(fil*3-(3-col))
                break
        if opc == 2:
            break              
         
            
 #INGRESO MENU OPCION 2 --- INGRESO DE DATOS PERSONALES -----------------------------------------------------------------------  
    if opcion_seleccionada == 2:
        print("Usted ha seleciconado la opcion 2.INGRESE DATOS PERSONALES PARA COMPRA DE ASIENTO")
        nom_comprador=input("Ingrese nombre comprador: ")
        apellido_comprador=input("Ingrese apellido del comprador: ")
        rut_comprador1=int(input("Ingrese el rut del comprador, sin puntos ni guion: "))
        correo_comprador=input("Ingrese correo del comprador: ")
         
        lista=["nom_comprador","apellido_comprador","rut_comprador","correo_comprador",fil*3-(3-col)]
        print("")
        arreglo=np.array(len(lista))
        for i in range(1):
            print(f"El nombre y apellido ingresado fueron: {nom_comprador} - {apellido_comprador}")
            print("Y el Rut es: ", rut_comprador1)
            print(f"Señor/a {nom_comprador} se sienta en el {fil*3-(3-col)}")
            print("El correo para envío de información es: ", correo_comprador)
        
        continue

#MENU OPCION 3 -------------------------------------------------------------------------     
    if opcion_seleccionada == 3:
        opc3()
        #print("1.EL ARO")
        #print("2.LA SIRENITA")
        #print("3.THE FLASH")
        #print("4.MARIO BROS")
        #ingreso_pelicula=int(input("seleccione una palicula: "))
        #if ingreso_pelicula==1:
        #    ingreso_pelicula="EL ARO"
        #    print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        #if ingreso_pelicula==2:
        #    ingreso_pelicula="LA SIRENITA"
        #    print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        #if ingreso_pelicula==3:
        #    ingreso_pelicula="THE FLASH"
        #    print("usted a seleccionado la pelicula: ", ingreso_pelicula)
        #if ingreso_pelicula==4:
        #    ingreso_pelicula="MARIO BROS"
        #    print("usted a seleccionado la pelicula: ", ingreso_pelicula)

#MENU OPCION 4 ---------------------------------------------------------------------------------------------
    if opcion_seleccionada == 4:
        opc4()
        #print("------------------BOLETA------------------")
        #print(f"El total de la compra es de:-----$ {monto_asiento}")
        #print("Usuari@ verá la pelicula: ",(ingreso_pelicula))
        #print(f"El asiento comprado es o son los Nª {lista_asiento}")
        #print("En el asiento numero: ",matrizbus)

#MENU OPCION 5 ----------------------------------------------------------------------------------------------

    if opcion_seleccionada == 5:
        print("Usted selecciono la opcion 5. SALIR")
        print("Munchas gracias por su compra\nHasta luego.")
        break