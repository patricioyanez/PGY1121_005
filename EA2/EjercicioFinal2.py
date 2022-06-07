print("\n****** Registro de persona ******")
nombre  = input("Ingrese su nombre: ")
edad    = input("Ingrese su edad  : ")
print("=== Ingreso de genero ===")
print("1.- Hombre")
print("2.- Mujer")
print("3.- Otro")
genero = input("Seleccione opción: ")
telefono = input("Ingrese nro de telefono:")

if genero == "1":
    print(f"Nombre: {nombre} y su edad es {edad}")
elif genero == "2":
    print(f"Nombre: {nombre} y su telefono es {telefono}")
else:
    print("No cumple con la opción del caso")