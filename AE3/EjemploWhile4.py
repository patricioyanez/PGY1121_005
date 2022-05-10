# 1.- DEFINIR VARIABLES
flag = True
# 2.- SOLICITAR LOS DATOS
print("\n ********* Invertir numero ********")
while flag:
    numero = int(input("Ingrese el número:"))
    if numero >= 103 and numero <= 987:
        flag = False

# 3.- PROCESAR LA INFO
unidad = int(numero / 100)
decena = int(numero / 10) - (unidad * 10)
centena= numero - (unidad * 100 + decena * 10)
numeroInvertido = centena*100 + decena*10 + unidad

# 4.- MOSTRAR EL RESULTADO
print("El valor es:", numeroInvertido)