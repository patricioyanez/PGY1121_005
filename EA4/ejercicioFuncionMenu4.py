# 0.- definir las funciones
def sumar(num1, num2):
    return num1 + num2
def restar(num1, num2):
    return num1 - num2
def dividir(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    return num1 // num2
def multiplicar(num1, num2):
    return num1 * num2

# 1.- DEFINIR VARIABLES
num1 = 0
num2 = 0
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
# 2.- SOLICITAR LOS DATOS
print("\n ********* Calculadora ********")
while opcion != "5":
    print("==== Menu principal ====")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in listaDeOpciones:
        input("La opción no es válida")
        input("Presione enter para continuar")
    elif opcion == "5":
        print("Adios!!!")
    else:
        num1 = int(input("Ingrese valor 1:")) 
        num2 = int(input("Ingrese valor 2:"))
        resultado = None
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = dividir(num1, num2)
        elif opcion == "4":
            resultado = multiplicar(num1, num2)

        print("El resultado es:", resultado)
        input("presione enter para continuar...")
    
