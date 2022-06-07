# solicitar las notas
nota1 = input("Ingrese nota 1: ")
nota2 = input("Ingrese nota 2: ")
nota3 = input("Ingrese nota 3: ")

# convertirlas en un numero (input devuelve un string)
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

# validamos que este dentro del rango del 1 al 7
if nota1 < 1 or nota1 > 7:
    print("Nota 1 no es válida")
elif nota2 < 1 or nota2 > 7:
    print("Nota 2 no es válida")
elif nota3 < 1 or nota3 > 7:
    print("Nota 3 no es válida")
else:
    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 4:
        print("Aprobado")
    else:
        print("Reprobado")

