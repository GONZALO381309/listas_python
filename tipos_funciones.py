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
