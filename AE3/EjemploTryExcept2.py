a = 5
b = 0
try:    
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("Error, no se puede dividir por cero")
except:
    print("Error en la app")
print("Fin del programa")