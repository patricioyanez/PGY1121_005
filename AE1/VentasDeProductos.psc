Algoritmo Venta
	// realizar la venta de 3 productos: Coca cola, Fanta y Sprite.
	//Los valores de estos son: 600, 500 y 350.
	// solicitar al usuario que producto quiere y la cantidad.
	// mostrar el total a pagar.
	Definir opcion Como Entero
	Definir totalPagar Como Entero
	Definir cantidad Como Entero
	// menu con los productos a vender
	Escribir "*** Maquina de bebidas ***"
	Escribir "1.- Coca cola $600"
	Escribir "2.- Fanta     $500"
	Escribir "3.- Sprite    $350"
	Escribir "Ingrese la opcion:"
	Leer opcion
	// pedir la cantidad de productos a comprar (del mismo)
	Escribir "Ingrese la cantidad de productos a compras"
	Leer cantidad
	// identificar cual producto selecciono el usuario
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
	
	
FinAlgoritmo
