#operaciones principales
def sumar(x, y):
    return x + y #devolver el resultado de las operaciones

def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

salir = 1

while(salir != 0):

    print("--------------------------------------------------")
    #mensajes para el usuario
    print("Elige una operación")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    #seleccionar las operaciones
    seleccion = input("Introduce un numero del 1 al 4: " )

    #variables para calcular
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))


    #uso de condiciones (se puede tambien con un switch)
    if seleccion == '1':
        print(num1, " + ", num2, " = ",  sumar(num1, num2))
    elif seleccion == '2':
        print(num1, " - ", num2, " = ",  restar(num1, num2))
    elif seleccion == '3':
        print(num1, " * ", num2, " = ",  multiplicar(num1, num2))
    elif seleccion == '4':
        if num2 == 0:
            print("No se puede divir entre 0")
        else:     
            print(num1, " / ", num2, " = ",  dividir(num1, num2))
    else:
        print("Seleccion equivocada")

    salir = int(input("Si desea salir presione 0..."))




