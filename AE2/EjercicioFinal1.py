# 1er definir variables y 2do solicitar datos
print("\n****** Calculo de numero mayor ******")
n1 = int(input("Ingrese nro 1: "))
n2 = int(input("Ingrese nro 2: "))
n3 = int(input("Ingrese nro 3: "))

# 3.- Procesar la información

if n1 > n2 and n1 > n3:
    print("el 1er nro es mayor")
elif n2 > n3:
    print("el 2do nro es mayor")
else:
    print("el 3er nro es mayor")