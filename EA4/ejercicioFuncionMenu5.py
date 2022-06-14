# usar cmd para instalar numpy
# pip install numpy
import numpy as nu
casillero = nu.array([["","",""],["","",""],["","",""]])

# 0.-  definir funciones
def arrendar(casillero):
    pass
def mostrarDisponible(casillero):
    pass
def mostrarClientes(casillero):
    pass
def mostrarGanancias(casillero):
    pass

# 1.- DEFINIR VARIABLES
filaCasillero = -1 # precio segun la fila seleccionada
posicionCasillero = -1 # posición dentro de la fila del 1 al 3 (restar 1 para indice)
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
# 2.- SOLICITAR LOS DATOS
print("\n ********* Calculadora ********")
while opcion != "5":
    print("==== Menu principal ====")
    print("1.- Arrendar casillero")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Ver nombres de clientes")
    print("4.- Mostrar ganancias")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in listaDeOpciones:
        input("La opción no es válida")
        input("Presione enter para continuar")
    elif opcion == "5":
        print("Adios!!!")
    else:
        if opcion == "1":
            arrendar(casillero)
        elif opcion == "2":
            mostrarDisponible(casillero)
        elif opcion == "3":
            mostrarClientes(casillero)
        elif opcion == "4":
            mostrarGanancias(casillero)
