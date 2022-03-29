Algoritmo VentaMaquinaMientras
	Definir opcion Como Entero
	Definir totalPagar Como Entero
	Definir cantidad Como Entero
	opcion = 0
	// menu con los productos a vender
	Mientras opcion <> 4 Hacer
		Limpiar Pantalla
		Escribir "*** Maquina de bebidas ***"
		Escribir "1.- Coca cola $600"
		Escribir "2.- Fanta     $500"
		Escribir "3.- Sprite    $350"
		Escribir "4.- Salir"
		Escribir "Ingrese la opcion:"
		Leer opcion
		
		si opcion = 4 Entonces
			Escribir "La maquina esta cerrada"			
		sino
			Escribir "Ingrese la cantidad de productos a compras"
			Leer cantidad
			si opcion = 1 Entonces
				totalPagar = cantidad * 600
			SiNo
				si opcion = 2 Entonces
					totalPagar = cantidad * 500
				SiNo
					totalPagar = cantidad * 350
				FinSi
			FinSi			
			Escribir "El total a pagar es: ", totalPagar
			Escribir "Presione enter para continuar"
			//Esperar Tecla
			Esperar 3 Segundos
		FinSi		
	FinMientras
	
FinAlgoritmo
