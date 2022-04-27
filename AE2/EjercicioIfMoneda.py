print("====== Convertidor de moneda ======")
print("1.- Dolar Australiano")
print("2.- Peso Argentino")
print("3.- Yen")
moneda = input("Seleccione la moneda a convertir: ")

cantidad = float(input("Ingrese la cantidad a convertir : "))
valor =  float(input("Ingrese el valor actual         : "))
total = int(cantidad * valor)
if moneda == "1":
    print("La cantidad dolar australiano en pesos es:", total)
elif moneda == "2":
    print("La cantidad peso argentino en pesos es:", total)
else:
    print("La cantidad de yenes en pesos es:", total)
