Algoritmo Descuentos
	Definir totalCompra Como Entero
	Definir totalAPagar Como Real
	
	Escribir "Ingrese el total de la compra"
	Leer totalCompra
	
	si totalCompra < 100 Entonces
		Escribir "El total es: ", totalCompra
	SiNo
		si totalCompra >= 500 Entonces
			totalAPagar = totalCompra * .7
			Escribir "El descuento es: 30%"
		SiNo
			si totalCompra >= 200 Entonces
				totalAPagar = totalCompra * .8
				Escribir "El descuento es: 20%"
			SiNo
				totalAPagar = totalCompra * .9
				Escribir "El descuento es: 10%"
			FinSi
		FinSi
		Escribir "El total es:", totalAPagar
	FinSi
	
	
FinAlgoritmo
