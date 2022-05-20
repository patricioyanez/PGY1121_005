try:
    numero = input("Ingrese un nro: ")
    if not type(numero) is int:
        raise("El valor no es un nro entero")
except:
    print("Error en la ejecución de la app")
print("App cerrada")
