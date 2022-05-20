a = 5
b = 10
try:    
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("Error, no se puede dividir por cero")
else:
    print("No ocurrio errores en el bloque TRY")

print("Fin del programa")