import numpy as nu

arreglo = nu.array([1,2,3,4])
print(arreglo)
arreglo = arreglo + 1
print(arreglo)
arreglo += 1
print(arreglo)
arreglo **= 2
print(arreglo)

arreglo = nu.ones(5)
print("crea arreglo y los llena con 1's", arreglo)
arreglo +=4
print("Suma 4 a todos los valores del arreglo ", arreglo)

arreglo2 = nu.ones(5)
print("Suma los valores de ambos arreglos: ",arreglo + arreglo2)

# compara si ambos arreglos tienen el mismo valor en cada uno de los 
# elementos

print("Resultado igualdad: ",arreglo == arreglo2)
arreglo3 = nu.array([1,5,5,3,1])
print("Resultado igualdad: ",arreglo == arreglo3)

print("Resultado mayor: ",arreglo > arreglo3)