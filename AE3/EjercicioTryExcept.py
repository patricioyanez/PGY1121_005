#Ejercicios:
# agregar try except, en donde sea necesario
# para evitar la "caida" de la app.
# usar el menú de panadería realizado en ejercicio anterior.
# 1.- DEFINIR VARIABLES
subTotal = 0
opcion = "0"
# 2.- SOLICITAR LOS DATOS
print("\n ********* Panadería ********")
while opcion != "6":
    print("==== Menu principal ====")
    print("1.- Pan amasado")
    print("2.- Pan Molde")
    print("3.- Pan Baguette")
    print("4.- Pan Integral")
    print("5.- Total venta")
    print("6.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in ("1","2","3","4","5","6"):
        input("La opción no es válida")
    elif opcion == "6":
        print("Adios!!!")
    elif opcion == "5":
        if subTotal < 5000:
            subTotal*=1.1
            print("La venta paga envío")
        else:
            print("El envío es gratis")
        print("El total de la venta es", int(subTotal)) 
        subTotal = 0
    else:
        try:
            cantidad = int(input("Ingrese cantidad de pan a llevar:")) 
        except ValueError:
            input("Dato ingresado no es correcto. Presione enter para volver.")            
            continue
        
        if opcion == "1":
            subTotal += cantidad * 1500
        elif opcion == "2":
            subTotal += cantidad * 1000
        elif opcion == "3":
            subTotal += cantidad * 2000
        elif opcion == "4":
            subTotal += cantidad * 3000
        print("El sub total es:", subTotal)

    

