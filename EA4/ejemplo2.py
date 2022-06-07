import numpy as nu

## metodos diponibles en numpy
arreglo = nu.arange(10)
print(arreglo)

arreglo = nu.arange(10.0)
print(arreglo)

arreglo = nu.arange(4, 15)
print(arreglo)

arreglo = nu.arange(2, 11, 2)
print(arreglo)

arreglo = nu.arange(1, 10, 2)
print(arreglo)
## asignacion de un arreglo a una variable
a = 1
b = a
b =2
print(a)
var = arreglo
var[0] = 100
print(arreglo[0])

var = arreglo.copy()
var[0] = 1
print(arreglo)
print(var)