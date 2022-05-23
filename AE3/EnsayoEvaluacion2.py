listadoCliente = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo = ""
suscripcion = True

opcion = 0

while opcion != 4:
    print("===== Menú ====")
    print("1. Registrar")
    print("2. Suscripción")
    print("3. Consultar")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese  opción:"))
    except:
        print("La opción no es correcta.")
        input("Presione enter para continuar....")
        continue

    
    if opcion < 1 or opcion > 4:
        print("La opción no es válida.")
        input("Presione enter para continuar....")
        continue
    elif opcion == 4:
        print("Adios.")
    else:
        if opcion == 1:
            print("opción seleccionada es 1")

            rut         = input("ingrese su rut         : ")
            nombre      = input("ingrese su nombre      : ")
            direccion   = input("ingrese su direccion   : ")
            comuna      = input("ingrese su comuna      : ")
            correo      = input("ingrese su correo      : ")
            edad        = input("ingrese su edad        : ")
            genero      = input("ingrese su genero      : ")
            celular     = input("ingrese su celular     : ")
            tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")
            
            tipoSeleccionado = ""
            if tipo == "1":
                tipoSeleccionado = "PREMIUM"
            elif tipo == "2":
                tipoSeleccionado = "GOLD"
            elif tipo == "3":
                tipoSeleccionado = "SILVER"
            else:
                continue

        elif opcion == 2:
            print("opción seleccionada es 2")
        elif opcion == 3:
            print("opción seleccionada es 3")
        
        input("Presione enter para continuar....")