print("****** Menú *******")
print("¿Qué animal que vive en el mar?")
print("1.- Perro")
print("2.- Cocodrilo")
print("3.- Conejo")
print("4.- Tiburón")
opcion = input("Seleccione opción: ")
puntos = 0
if opcion == "2":
    puntos = .5
elif opcion == "4":
    puntos = 1

print("Puntaje total: ", puntos )