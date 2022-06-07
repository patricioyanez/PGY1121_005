print("Calculo de la formula")
x = input("Ingrese el valor de la X: ") # input devuelve un string
# convertir texto en un numero
x = int(x) #  int("4") ==> 4
resultado = (x**2 + 3*x + 1) / 4
print("El resultado es:", resultado)