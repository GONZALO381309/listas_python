encendido=True
opcion=0
def suma(num_1:int,num_2:int):
    return num_1+num_2

def resta(num_1:int,num_2:int):
    return num_1-num_2

def multiplicacion(num_1:int,num_2:int):
    return num_1*num_2

def division(num_1:int,num_2:int):
    return num_1/num_2

while encendido:
    print("***CALCULADORA***\n")
    print("1.-Sumar 2 numeros")
    print("2.-Restar 2 numeros")
    print("3.-Multiplicar 2 numeros")
    print("4.-Dividir 2 numeros")
    print("5.-Salir")
    opcion=int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("Selecciono opcion: ", opcion)
        num_1=int(input("Ingrese primer numero: "))
        num_2=int(input("Ingrese segundo numero: "))
        print("La suma de los numeros es: ", suma(num_1,num_2))
            
    if opcion == 2:
        print("Selecciono opcion: ", opcion)
        num_1=int(input("Ingrese primer numero: "))
        num_2=int(input("Ingrese segundo numero: "))
        print("La resta de los numeros es: ", resta(num_1,num_2))
    if opcion == 3:
        print("Selecciono opcion: ", opcion)
        num_1=int(input("Ingrese primer numero: "))
        num_2=int(input("Ingrese segundo numero: "))
        print("La multiplicacion de los numeros es: ", multiplicacion(num_1,num_2))
    if opcion == 4:
        print("Selecciono opcion: ", opcion)
        num_1=int(input("Ingrese primer numero: "))
        num_2=int(input("Ingrese segundo numero: "))
        print("La division de los numeros es: ", division(num_1,num_2))
    if opcion == 5:
        print("Selecciono opcion: ", opcion)

    break

encendido=False