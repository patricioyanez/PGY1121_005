def sumar(a,b):
    total = a + b
    print(f"El total es:{total}")

def sumar1(a,b):
    total = a + b
    return total

num1 = int(input("Ingrese nro 1:"))
num2 = int(input("Ingrese nro 2:"))

sumar(num1, num2)

print("El total de la suma es:", sumar1(num1, num2))