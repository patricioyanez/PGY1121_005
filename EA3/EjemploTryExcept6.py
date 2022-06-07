try:
    numero = int(input("Ingrese un nro: "))
except ValueError:
    print("Tipo de datos no es el correcto")
except:
    print("Error en la ejecución de la app")
    
print("App cerrada")