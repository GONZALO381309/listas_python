#Sistema Impresión DUOC
#Iniciar sesión
#Mostrar el menú
    #Opciones   
    #1. Impresión
        #1.1. BN $150
        #1.2 color $300
    #2. Fotocopias $80
    #3. Anillados $5.000
    #4. Pago
    #5. Anular
    #6. Salir

#Declaración de variables
usuario_guardado1="gonza"
password_guardado1=12
usuario_guardado2="alumno"
password_guardado2=1234
opcion=0
opcion_impresion=0
opcion_modalidad=0
opcion_pago_dividido=0
menu_activo=True
#inicializar las variables
cantidad_bn=0
cantidad_color=0
cantidad_fotocopia=0
cantidad_anillados=0
#Valores
valor_bn=150
valor_color=300
valor_fotocopia=80
valor_anillados=5000
#totales
total_bn=0
total_color=0
total_fotocopia=0
total_anillados=0

#totales
total_bn_final=0
total_color_final=0
total_fotocopia_final=0
total_anillados_final=0

aplicar_descuento=0


print("Bienvenido al sistema de impresión DUOC")
print("Inicie sesión")

usuario_entrante=input("Ingrese su usuario: ")
password_entrante=int(input("Ingrese su contrtaseña: "))
#el usuario 1 es correcto
if(usuario_entrante==usuario_guardado1 and password_entrante==password_guardado1 or usuario_entrante==usuario_guardado2 and password_entrante==password_guardado2):
    while menu_activo :
        print(""" 
            1. Impresión 
            2. Fotocopias $80
            3. Anillados $5.000
            4. Pago
            5. Anular
            6. Salir """)
        print()
        opcion=int(input("Seleccione una opción: "))
        if(opcion<1 or opcion>6):
            print("La opción ingresada no es valida")
        else:    
            if opcion == 1 :
                print("Seleccionó la Impresión")
                opcion_impresion=int(input(""""
                1.- BN $150
                2.- Color $300
                """))
                if opcion_impresion < 1 and opcion_impresion > 2 :
                    print("La opción ingresada no es valida")
                else:
                    if opcion_impresion == 1 :
                        print("Seleccionó BN $150")
                        cantidad_bn=int(input("Ingrese la cantidad: "))
                        total_bn = total_bn + cantidad_bn*valor_bn

                    if opcion_impresion == 2 :
                        print("Seleccionó Color $300")
                        cantidad_color=int(input("Ingrese la cantidad: "))
                        total_color =  total_color + cantidad_color * valor_color
                  
            if opcion == 2 :
                print("Seleccionó la Fotocopias $80")
                cantidad_fotocopia=int(input("Ingrese la cantidad: "))
                total_fotocopia = total_fotocopia + cantidad_fotocopia * valor_fotocopia
                
            if opcion == 3 :
                print("Seleccionó el Anillados $5.000")
                cantidad_anillados=int(input("Ingrese la cantidad: "))
                total_anillados = total_anillados + cantidad_anillados * valor_anillados
            
            if opcion == 4 :
                print("Seleccionó Pago")
                opcion_modalidad=int(input("""Seleccione su modalidad de descuento:
                    1.- Diurno
                    2.- Vespertino
                    3.- Administrativo
                """))
                if opcion_modalidad == 1 :
                    aplicar_descuento= 0.1 
                if opcion_modalidad == 2 :
                    aplicar_descuento= 0.2
                if opcion_modalidad == 2 :
                    aplicar_descuento= 1
                opcion_pago_dividido=int(input("Quiere dividir el pago?\n ingrese el número de personas\nIngrese 1 para no dividr pago"))
                total_sin_descuento=total_bn+total_color+total_fotocopia+total_anillados
                total_con_descuento=total_sin_descuento*aplicar_descuento
                #calcular los totales
                print("   Servicio de Fotocopiado   ")
                print("-----------------------------")
                print(f"{total_bn/valor_bn} hojas B/N {total_bn}")
                print(f"{total_color/valor_color} hojas color {total_color}")
                print(f"{total_fotocopia/valor_fotocopia} hojas fotocopia {total_fotocopia}")
                print(f"{total_anillados/valor_anillados} anillados {total_anillados}")
                print(f"Subtotal {total_sin_descuento}")
                print(f"Descuento {aplicar_descuento*100}% ${total_con_descuento}")
                
                x = range(opcion_pago_dividido)
                for n in x :
                    print(f"Total a pagar {n+1} ${total_con_descuento/opcion_pago_dividido}")
                print("Gracias por su compra")
                menu_activo=False 
               
            if opcion == 5 :
                print("Seleccionó Anular")
                #Valores
                valor_bn=150
                valor_color=300
                valor_fotocopia=80
                valor_anillados=5000
                #totales
                total_bn=0
                total_color=0
                total_fotocopia=0
                total_anillados=0

                #totales
                total_bn_final=0
                total_color_final=0
                total_fotocopia_final=0
                total_anillados_final=0

                aplicar_descuento=0
            
            if opcion == 6 :
                print("Seleccionó Salir")
                menu_activo=False       
    print("Gracias por preferirnos")  
else:
    print("Usuario o contraseña incorrecta.")
