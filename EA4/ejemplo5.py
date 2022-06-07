import numpy as np

# creación de arreglo de 2 dimensiones
arrayBidimensional = np.array([[1,2,3],[9,8,7]])
print(arrayBidimensional)


print("suma :", arrayBidimensional.sum())
print("Mayor:", arrayBidimensional.max())
print("Menor:", arrayBidimensional.min())
print("Prom :", arrayBidimensional.mean())

print("valor coordenadas:", arrayBidimensional[1,0]  )

# usar todas las propiedades y metodos vistos con los 
# arreglos unidimensional