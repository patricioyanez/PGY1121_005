clientes = []
rut = 6000000
nombre = "Ana"
direccion = "Americo vespucio 1501"
comuna = "Cerrillos"
correo = "ana@mail.com"
edad = -1
genero = "F"
celular ="546546"
tipo = "PREMIUM"
suscripcion = True
fecha = "24-05-2022"

cliente = [rut, nombre, direccion, comuna, correo, edad,genero,celular,tipo, suscripcion,fecha]
clientes.append(cliente)
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

            try:
                rut = int(input("ingrese su rut          : "))

                if rut < 5000000 or rut > 99999999:
                    raise("Rut fuera de rango")    
            except:
                print("Rut no válido")
                input("Presione enter para continuar....")
                continue

            nombre      = input("ingrese su nombre       : ")
            direccion   = input("ingrese su direccion    : ")
            comuna      = input("ingrese su comuna       : ")
            correo      = input("ingrese su correo       : ")
            if correo.find("@") == -1:
                print("Correo no válido")
                input("Presione enter para continuar....")
                continue
            try:
                edad        = int(input("ingrese su edad         : "))            
                if edad < 0 or edad > 110:
                    raise("Edad fuera de rango")    
            except:
                print("Edad no válido")
                input("Presione enter para continuar....")
                continue

            genero      = input("ingrese su genero(F o M): ")
            if genero != 'F' and genero != 'M':
                print("Genero no válido")
                input("Presione enter para continuar....")
                continue

            celular     = input("ingrese su celular      : ")
            tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")
            
            if tipo == "1":
                tipo = "PREMIUM"
            elif tipo == "2":
                tipo = "GOLD"
            elif tipo == "3":
                tipo = "SILVER"
            else:
                print("Tipo no válido")
                input("Presione enter para continuar....")
                continue
            cliente = [rut, nombre, direccion, comuna, correo, edad,genero,celular,tipo, suscripcion]

            clientes.append(cliente)

        elif opcion == 2:
            print("opción seleccionada es 2")
            try:
                rut = int(input("ingrese su rut          : "))

                if rut < 5000000 or rut > 99999999:
                    raise("Rut fuera de rango")    
            except:
                print("Rut no válido")
                input("Presione enter para continuar....")
                continue
            
            fueEncontrado = False
            for cliente in clientes:
                if cliente[0] == rut:
                    cliente.append("24-05-2022")
                    fueEncontrado = True
                    break
            
            if not fueEncontrado:
                print("Rut de cliente no encontrado")

        elif opcion == 3:
            print("opción seleccionada es 3")
            try:
                rut = int(input("ingrese su rut          : "))

                if rut < 5000000 or rut > 99999999:
                    raise("Rut fuera de rango")    
            except:
                print("Rut no válido")
                input("Presione enter para continuar....")
                continue
            
            clienteEncontrado = []
            for cliente in clientes:
                if cliente[0] == rut:
                    clienteEncontrado = cliente
                    break
            
            if len(clienteEncontrado) == 0:
                print("Rut de cliente no encontrado")
            else:
                print("\n==== Datos del usuario encontrado ====")
                print("Rut              :", clienteEncontrado[0])
                print("Nombre           :", clienteEncontrado[1])
                print("Dirección        :", clienteEncontrado[2])
                print("Comuna           :", clienteEncontrado[3])
                print("Correo           :", clienteEncontrado[4])
                print("Edad             :", clienteEncontrado[5])
                print("Genero           :", clienteEncontrado[6])
                print("Celular          :", clienteEncontrado[7])
                print("Tipo             :", clienteEncontrado[8])
                print("Fecha Suscripción:", clienteEncontrado[10])

        input("Presione enter para continuar....")