# 1- definir las variables
subTotal = 0
descuento= 0
valor    = 0
total    = 0

# 2- solicitar los datos al usuario
print("******  Super Cine Duoc Plaza Oeste ********")
print("Pertenece a DUOC UC PO")
print("1.- SI")
print("2.- No")
esDeDuoc = input("Seleccione opción: ")

print("==== Tipo de Entrada =====")
print("1.- Estreno")
print("2.- Normal")
tipoEntrada = input("Seleccione opción: ")
cantidadTipoEntrada = input("Ingrese cantidad: ")

print("==== Palomitas =====")
print("1.- Pequeña")
print("2.- Media")
print("3.- Grande")
palomitas = input("Seleccione opción: ")
cantidadPalomitas = input("Ingrese cantidad: ")

print("==== Bebidas =====")
print("1.- Pequeña")
print("2.- Media")
print("3.- Grande")
bebidas = input("Seleccione opción: ")
cantidadBebidas = input("Ingrese cantidad: ")

# 3.-Procesar la info entreda por el usuario

if tipoEntrada == "1":
    valor = 4800
else:
    valor = 2900

subTotal = valor * int(cantidadTipoEntrada)

if palomitas == "1":
    valor = 2500
elif palomitas == "2":
    valor = 4500
else:
    valor = 7800

subTotal = subTotal +  valor * int(cantidadPalomitas)

if bebidas == "1":
    valor = 1000
elif bebidas == "2":
    valor = 1250
else:
    valor = 2000

subTotal = subTotal +  valor * int(cantidadBebidas)

if esDeDuoc == "1":
    descuento = subTotal * .3

# 4.- Mostrar resultados
print("=== Total de la compra ====")
print("Subtotal   : ", subTotal)
print("descuento  : ", descuento)
print("Total      : ", (subTotal-descuento))