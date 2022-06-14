# usar cmd para instalar numpy
# pip install numpy
import numpy as nu
casillero = nu.array([["","",""],["","",""],["","",""]])

# 0.-  definir funciones
def arrendar(casillero):
    print("*** Arrendar casillero ****")
    print("Ingrese nivel del casillero")
    print("Nivel 1. $10000")
    print("Nivel 2. $5000")
    print("Nivel 3. $2000")
    opcion = 0
    try:
        opcion = int(input("Ingrese opción:"))
        fila = opcion - 1
        mostrarCasillerosFila(casillero, fila)
        nroCasillero = int(input("ingrese casillero a utilizar"))
        columna = nroCasillero - 1
        nombre = input("Ingrese su nombre para la reserva:")
        casillero[fila, columna] = nombre
    except:
        print("Error en el ingreso de opción")
        input("Presione enter para volver al menú")
        return

def mostrarCasillerosFila(casillero, fila):
    nroCasillero = 1
    listado = ""
    print("Casilleros disponible en la fila:", fila+1)
    for columna in casillero[fila]:
        if columna == "": # si no hay nombres esta desocupado
            listado += str(nroCasillero) + "\n"
        nroCasillero+=1
    print(listado)

def mostrarDisponible(casillero):
    print("Disponibilidad de los casilleros")
    listado = ""
    nroCasillero = 1
    valor = ""    
    for fila in casillero:
        for columna in fila:
            if columna != "":
                valor = "x"
            else:
                valor = nroCasillero
            listado += str(valor) + " "
            nroCasillero += 1
        listado += "\n"
    print(listado)
    input("Presione enter para volver al menú...")

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
