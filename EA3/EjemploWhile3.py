# 1.- DEFINIR VARIABLES
acumulador = 0
contador = 1
# 2.- SOLICITAR LOS DATOS
# 3.- PROCESAR LA INFO
print("\n ********* Suma de numeros ********")
while contador <= 5:
    numero = int(input("Ingrese el número:"))
    if numero > 0:
        acumulador += numero
        contador += 1 # contador = contador +1
# 4.- MOSTRAR EL RESULTADO
print("El factorial es:", acumulador)