def calculo(precio , descuento):
    return precio - (precio * descuento / 100)

datos = [10000, 15]
print("Total a pagar es:", calculo(*datos))

# valores a entregar al llamar a la función
datos = [25000, 10]
# el signo *, permite asignar valores a los parametros a partir de una lista
print("Total a pagar es:", calculo(*datos)) 