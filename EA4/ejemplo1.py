import numpy
arreglo = numpy.array([1,4,5,6,78,9,100,2])
print(arreglo)

print("Cantidad de dimensiones:", arreglo.ndim)
print("Cantidad de elementos:", arreglo.shape)
print("Cantidad de elementos:", len(arreglo))

# acceder a los elementos del arreglo
# permite mostrar los 2 primeros elementos
print("Valor del primer elemento:", arreglo[0])
print("Valor del 2do elemento:", arreglo[1])


# permite mostrar los 2 últimos elementos
print("Valor del primer elemento:", arreglo[-1])
print("Valor del 2do elemento:", arreglo[-2])

# permite obtener una porción del arreglo
print("Obtiene los siguientes elementos:", arreglo[3:6])
print("Obtiene los siguientes elementos:", arreglo[:6])
print("Obtiene los siguientes elementos:", arreglo[3:])
print("Obtiene los siguientes elementos:", arreglo[3:])

print("Obtiene los elementos:", arreglo[2:7:2])
print("Obtiene los elementos:", arreglo[2::3])
print("Obtiene los elementos:", arreglo[:5:3])






