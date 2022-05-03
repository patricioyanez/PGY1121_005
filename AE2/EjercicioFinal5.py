# 1.- variables
total = 0
# 2.- solicitar info
print("\n****** Fabrica de mascarillas ******")
cantidad = int(input("Ingrese cantidad de mascarillas a comprar:"))
total = cantidad * 500

if total < 15000:
    print("=== Opciones de envio ===")
    envio = int(input("1.- Misma comuna 2.- Comuna aledaña 3.- otro: "))
    if envio == 1:
        total += 1000
    elif envio == 2:
        total += 2000
    else:
        total += 3000

print("Total a pagar es:", format(total, ',d'))