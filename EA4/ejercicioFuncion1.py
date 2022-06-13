def resta(a =None, b=None):
    if a == None or b == None:
        print("Error en los datos")
        return # finalizar la ejecución de la función
    return a - b

resta()
resta(1)
print("La resta es:", resta(2,1))
print("La resta es:", resta(20,10))
print("La resta es:", resta(50,5))
print("La resta es:", resta(30,1))