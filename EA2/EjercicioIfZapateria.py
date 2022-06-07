print("=====  Zapateria DuocUC PO =====")
talla = input("Ingrese la talla  del calzado: ")
cantidad = int(input("Ingrese la cantidad a comprar: "))

total = cantidad * 20000
envio = 0
if total < 40000:
    envio = 3000 # total += 3000

print("El total a pagar es:", total)

if envio != 0:
    print("costo del envio:", envio)
else:
    print("El costo del envio es gratis :)")