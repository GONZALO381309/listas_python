opcion=0
menu_act=True
precio_real=0
desc_al_total=0


def calcular_iva(valor_producto:int):
   return valor_producto*0.19

def descuento(precio_real,desc_al_total):
    return precio_real-desc_al_total

while menu_act:
    print("1. Calcule el IVA")
    print("2. Valor descuento")
    print("3. Calcule su IMC")
    print("4. Salir")

    opcion=int(input("Elija una opcion: "))

    if opcion == 1:
        print("Selecciono opcion: ", opcion)
        valor_producto=int(input("Ingrese el precio del producto: "))
        print("El iva corresponde a: ",calcular_iva(valor_producto))
    
    if opcion == 2:
        print("Selecciono opcion: ", opcion)
        precio=int(input("Ingrese el precio del producto: "))
        print("El iva corresponde a: ",descuento(precio_real,desc_al_total))

    if opcion == 4:
        print("Selecciono opcion: ", opcion)
        print("Ha salido del sistema")
        print("Muchas gracias")
        break


menu_act=False








