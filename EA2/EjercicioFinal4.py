# 1.- variables
total = 0
# 2.- solicitar info
print("\n****** Delivery SandWich ******")
churrascos  = int(input("Ingrese cantidad de churrascos : "))
completos   = int(input("Ingrese cantidad de completos  : "))
vegetariano = int(input("Ingrese cantidad de vegetariano: "))
barrosLuco  = int(input("Ingrese cantidad de barros luco: "))
tieneDescuento = int(input("Tiene código de descuento 1.-Si 2.- No:"))

# 3.- procesar info
total = churrascos * 1500
total += completos * 1000
total += vegetariano * 2000
total += barrosLuco * 3000 # total = total + amonio * 3000

if tieneDescuento == 1:
    total *= .9

#4.- mostrar resultados
print("El total a pagar es:", format(int(total), ',d'))