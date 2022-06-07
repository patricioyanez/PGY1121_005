# 1.- variables
total = 0
# 2.- solicitar info
print("\n****** Venta de artículos de limpieza ******")
mascarilla = int(input("Ingrese cantidad de mascarillas clínicas: "))
guantes = int(input("Ingrese cantidad de guantes clínicas    : "))
delantal = int(input("Ingrese cantidad de delantal clínicas   : "))
amonio = int(input("Ingrese cantidad de amonio cuaternario  : "))
descuento = int(input("Ingrese descuento: "))
# 3.- procesar info
total = mascarilla * 1000
total += guantes * 1000
total += delantal * 2000
total += amonio * 3000 # total = total + amonio * 3000
if descuento>0:
    total -= total * descuento / 100

#4.- mostrar resultados
print("El total a pagar es:", format(int(total), ',d'))