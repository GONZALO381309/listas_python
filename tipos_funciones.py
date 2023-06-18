#SIN ARGUMENTO Y SIN RETORNO
def saludo():
    print("Saludando a mis estudiantes")
saludo()

#SIN ARGUMENTO Y CON RETORNO
def suma1():
    num_1=10
    num_2=5
    resultado=num_1+num_2
    return resultado

resultado_suma=suma1()
print("Forma A de utilizar funcion con retorno",resultado_suma)
print("Forma B de utilizar funcion con retorno",suma1())

#CON ARGUMENTOS Y SIN RETORNO
def resta1(num_1, num_2):
    resultado=num_1-num_2
    print("El resultado de la resta es: ",resultado)
resta1(10,1)

def resta2(num_1, num_2):
    resultado=num_1-num_2
    return resultado
resultado1=resta2(10,1)
ressultado2=resta2(8,3)
#FORMA DECENTE
print(resultado1-ressultado2)
