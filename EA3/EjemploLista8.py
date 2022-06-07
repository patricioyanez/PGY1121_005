lista = [3,6,1,5,8,2,4]
print("Cantidad de elementos:",len(lista))
lista2= lista.copy()
lista3= lista
lista3[0] = 300
print(lista2)
print(lista3)
print(lista)