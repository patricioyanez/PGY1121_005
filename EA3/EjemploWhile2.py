# 1.- DEFINIR VARIABLES
acumulador = 1
contador = 1
# 2.- SOLICITAR LOS DATOS
print("\n ********* Calculo de factorial ********")
numero = int(input("Ingrese el número:"))
# 3.- PROCESAR LA INFO
while contador <= numero:
    acumulador *= contador
    contador += 1 # contador = contador +1
# 4.- MOSTRAR EL RESULTADO
print("El factorial es:", acumulador)